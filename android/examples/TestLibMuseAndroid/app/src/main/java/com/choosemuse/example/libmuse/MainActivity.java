/**
 * Example of using libmuse library on android.
 * Interaxon, Inc. 2016
 */

package com.choosemuse.example.libmuse;


import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;
import java.io.IOException;


import java.io.File;
import java.lang.ref.WeakReference;
import java.security.PublicKey;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import java.util.Map;
import java.util.concurrent.atomic.AtomicReference;

import com.android.volley.Cache;
import com.android.volley.Network;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.BasicNetwork;
import com.android.volley.toolbox.DiskBasedCache;
import com.android.volley.toolbox.HurlStack;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.choosemuse.libmuse.Accelerometer;
import com.choosemuse.libmuse.AnnotationData;
import com.choosemuse.libmuse.ConnectionState;
import com.choosemuse.libmuse.Eeg;
import com.choosemuse.libmuse.LibmuseVersion;
import com.choosemuse.libmuse.MessageType;
import com.choosemuse.libmuse.Muse;
import com.choosemuse.libmuse.MuseArtifactPacket;
import com.choosemuse.libmuse.MuseConfiguration;
import com.choosemuse.libmuse.MuseConnectionListener;
import com.choosemuse.libmuse.MuseConnectionPacket;
import com.choosemuse.libmuse.MuseDataListener;
import com.choosemuse.libmuse.MuseDataPacket;
import com.choosemuse.libmuse.MuseDataPacketType;
import com.choosemuse.libmuse.MuseFileFactory;
import com.choosemuse.libmuse.MuseFileReader;
import com.choosemuse.libmuse.MuseFileWriter;
import com.choosemuse.libmuse.MuseListener;
import com.choosemuse.libmuse.MuseManagerAndroid;
import com.choosemuse.libmuse.MuseVersion;
import com.choosemuse.libmuse.Result;
import com.choosemuse.libmuse.ResultLevel;

import android.Manifest;
import android.app.Activity;
import android.app.AlertDialog;
import android.app.DownloadManager;
import android.content.Context;
import android.content.DialogInterface;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.os.Environment;
import android.os.Looper;
import android.os.Handler;
import android.service.voice.VoiceInteractionSession;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TabHost;
import android.widget.TextView;
import android.bluetooth.BluetoothAdapter;


import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;





/**
 * This example will illustrate how to connect to a Muse headband,
 * register for and receive EEG data and disconnect from the headband.
 * Saving EEG data to a .muse file is also covered.
 * <p>
 * For instructions on how to pair your headband with your Android device
 * please see:
 * http://developer.choosemuse.com/hardware-firmware/bluetooth-connectivity/developer-sdk-bluetooth-connectivity-2
 * <p>
 * Usage instructions:
 * 1. Pair your headband if necessary.
 * 2. Run this project.
 * 3. Turn on the Muse headband.
 * 4. Press "Refresh". It should display all paired Muses in the Spinner drop down at the
 * top of the screen.  It may take a few seconds for the headband to be detected.
 * 5. Select the headband you want to connect to and press "Connect".
 * 6. You should see EEG and accelerometer data as well as connection status,
 * version information and relative alpha values appear on the screen.
 * 7. You can pause/resume data transmission with the button at the bottom of the screen.
 * 8. To disconnect from the headband, press "Disconnect"
 */


public class MainActivity extends Activity implements OnClickListener {

    private static final String FILE_NAME = "muse_data.txt";


    /**
     * Tag used for logging purposes.
     */
    private final String TAG = "TestLibMuseAndroid";

    /**
     * The MuseManager is how you detect Muse headbands and receive notifications
     * when the list of available headbands changes.
     */
    private MuseManagerAndroid manager;

    /**
     * A Muse refers to a Muse headband.  Use this to connect/disconnect from the
     * headband, register listeners to receive EEG data and get headband
     * configuration and version information.
     */
    private Muse muse;


    /**
     * The ConnectionListener will be notified whenever there is a change in
     * the connection state of a headband, for example when the headband connects
     * or disconnects.
     * <p>
     * Note that ConnectionListener is an inner class at the bottom of this file
     * that extends MuseConnectionListener.
     */
    private ConnectionListener connectionListener;

    /**
     * The DataListener is how you will receive EEG (and other) data from the
     * headband.
     * <p>
     * Note that DataListener is an inner class at the bottom of this file
     * that extends MuseDataListener.
     */
    private DataListener dataListener;

    /**
     * Data comes in from the headband at a very fast rate; 220Hz, 256Hz or 500Hz,
     * depending on the type of headband and the preset configuration.  We buffer the
     * data that is read until we can update the UI.
     * <p>
     * The stale flags indicate whether or not new data has been received and the buffers
     * hold the values of the last data packet received.  We are displaying the EEG, ALPHA_RELATIVE
     * and ACCELEROMETER values in this example.
     * <p>
     * Note: the array lengths of the buffers are taken from the comments in
     * MuseDataPacketType, which specify 3 values for accelerometer and 6
     * values for EEG and EEG-derived packets.
     */
    private final double[] eegBuffer = new double[6];
    private boolean eegStale;
    private final double[] alphaBuffer = new double[6];
    private boolean alphaStale;
    private final double[] accelBuffer = new double[3];
    private boolean accelStale;

    //add other buffers too

    private final double[] betaBuffer = new double[6];
    private boolean betaStale;

    private final double[] thetaBuffer = new double[6];
    private boolean thetaStale;

    private final double[] alphaAbsoluteBuffer = new double[6];
    private boolean alphaAbsoluteStale;

    private final double[] betaAbsoluteBuffer = new double[6];
    private boolean betaAbsolsulteStale;

    private final double[] thetaAbsoluteBuffer = new double[6];
    private boolean thetaAbsolsulteStale;


    private final double[] hci_precision = new double[4];

    private final double[] isGood = new double[4];


    /**
     * We will be updating the UI using a handler instead of in packet handlers because
     * packets come in at a very high frequency and it only makes sense to update the UI
     * at about 60fps. The update functions do some string allocation, so this reduces our memory
     * footprint and makes GC pauses less frequent/noticeable.
     */
    private final Handler handler = new Handler();

    /**
     * In the UI, the list of Muses you can connect to is displayed in a Spinner object for this example.
     * This spinner adapter contains the MAC addresses of all of the headbands we have discovered.
     */
    private ArrayAdapter<String> spinnerAdapter;

    /**
     * It is possible to pause the data transmission from the headband.  This boolean tracks whether
     * or not the data transmission is enabled as we allow the user to pause transmission in the UI.
     */
    private boolean dataTransmission = true;

    /**
     * To save data to a file, you should use a MuseFileWriter.  The MuseFileWriter knows how to
     * serialize the data packets received from the headband into a compact binary format.
     * To read the file back, you would use a MuseFileReader.
     */
    //private final AtomicReference<MuseFileWriter> fileWriter = new AtomicReference<>();
    private final AtomicReference<OutputStreamWriter> fileWriter = new AtomicReference<>();
    private final AtomicReference<FileOutputStream> fileWriter2 = new AtomicReference<>();
    /**
     * We don't want file operations to slow down the UI, so we will defer those file operations
     * to a handler on a separate thread.
     */
    private final AtomicReference<Handler> fileHandler = new AtomicReference<>();


    //--------------------------------------
    // Lifecycle / Connection code


    //192.168.178.161
    String url = "http://192.168.0.100/api/2PmPIT8bygMPV9M3WFKLHRLJ8zzep0wHycysuq29/lights/4/state";
    Map<String, Object> params = new HashMap<String, Object>();
    JSONObject jsonObject;

    ArrayList<Double> engagementArray = new ArrayList<>();

    long startTime;
    long endTime;
    long timeDifference;


    //to start with white color and no saturation

    int hue = 65535;
    int sat = 170;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // We need to set the context on MuseManagerAndroid before we can do anything.
        // This must come before other LibMuse API calls as it also loads the library.
        manager = MuseManagerAndroid.getInstance();
        manager.setContext(this);

        Log.i(TAG, "LibMuse version=" + LibmuseVersion.instance().getString());

        WeakReference<MainActivity> weakActivity =
                new WeakReference<MainActivity>(this);
        // Register a listener to receive connection state changes.
        connectionListener = new ConnectionListener(weakActivity);
        // Register a listener to receive data from a Muse.
        dataListener = new DataListener(weakActivity);
        // Register a listener to receive notifications of what Muse headbands
        // we can connect to.
        manager.setMuseListener(new MuseL(weakActivity));

        // Muse 2016 (MU-02) headbands use Bluetooth Low Energy technology to
        // simplify the connection process.  This requires access to the COARSE_LOCATION
        // or FINE_LOCATION permissions.  Make sure we have these permissions before
        // proceeding.
        ensurePermissions();

        // Load and initialize our UI.
        initUI();

        // Start up a thread for asynchronous file operations.
        // This is only needed if you want to do File I/O.
        fileThread.start(); 

        //create the first line of muse_data.txt


        // Start our asynchronous updates of the UI.
        handler.post(tickUi);


        RequestQueue queue = Volley.newRequestQueue(this);


        //get the infos about light status
        StringRequest stringRequest = new StringRequest(Request.Method.GET, url, new Response.Listener<String>() {

        @Override

        public void onResponse(String response) {

        // Display the response
        Log.i(TAG, "Response is: " + response);


        }

        }, new Response.ErrorListener() {
        @Override

        public void onErrorResponse(VolleyError error) {
        Log.i(TAG,"That didn't work!");
        }
        });

         params.put("on", true);
         params.put("hue", hue);
         params.put("sat", sat);

        jsonObject = new JSONObject(params);

        //jsonObject = null;

        //TODO:Thing about the order, first param.put() then this part or write it in another function

        JsonArrayRequest jsonArrReq = new JsonArrayRequest(Request.Method.PUT, url, jsonObject, new Response.Listener<JSONArray>() {


            @Override
            public void onResponse(JSONArray response) {
                Log.d("JSONPost", response.toString());


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.d("JSONPost", "Error:" + error.getMessage());

            }
        });

        queue.add(jsonArrReq);

        //queue.start();
        queue.add(stringRequest);

    }

    public void changeTheLight() {

        /**value between 0 and 65535. Both 0 and 65535 are red,
         *
         *
         * 25500 is green and 46920 is blue. value between 0 and 65535. Both 0 and 65535 are red,
         * 25500 is green and 46920 is blue **/

        //TODO:check how often the packet comes

        startTime = System.currentTimeMillis();


        //Map<String ,String> params = new HashMap<String, String>()


        //electrodes on the forehead
        double betaAverage = (betaBuffer[1] + betaBuffer[2]) / 2;
        double alphaAverage = (alphaBuffer[1] + alphaBuffer[2]) / 2;
        double thetaAverage = (thetaBuffer[1] + thetaBuffer[2]) / 2;

        double engagementLevel = betaAverage / alphaAverage + thetaAverage;
        //distracted : a while loop to decrement or increment Hue gradually

        //keep adding elements into the array until it is full with 1000
        //TODO: 2-3 minutes computing the average
        if (engagementArray.size() < 500 ) {
            engagementArray.add(engagementLevel);
        }


        if (engagementArray.size() == 500) {

            double sum = 0;
            double engagementAverage = 0;
            //TODO:calculate an average of all 1000 engagements

            for(int n=0; n < engagementArray.size(); n++) {
                sum += engagementArray.get(n);
            }


            engagementAverage = sum /engagementArray.size();


            engagementArray.clear();

            //TODO:find out an strategy to reduce saturation
            //TODO:check how blue the 46920 is and how much it can increase remaining blue

            /**case 1: good concentration
             * */
            if (engagementAverage >= 0.5) {
                Log.i(TAG, "good concentration");

                //TODO:how strong is sat:180 in a white room → need to be tested in the room
                if(sat > 180) {
                    sat = 180;
                    Log.i(TAG, "sat is: "+ sat);
                    params.put("sat", sat);
                    jsonObject = new JSONObject(params);
                    sendRequest();
                }


                /**increase saturation up to 155
                if (sat < 155) {
                    sat += 5;https://www.youtube.com/watch?v=YTRiH_rzDUw
                    params.put("sat", sat);
                    jsonObject = new JSONObject(params);
                    sendRequest();
                }**/
                if (hue < 46920) {
                    //increase saturation gradually to help staying focused
                    hue += 500;
                    Log.i(TAG, "hue is(good concentration): "+ hue);
                    params.put("hue", hue);
                    jsonObject = new JSONObject(params);
                    sendRequest();
                }

                //in case hue is red
                if (hue > 46920) {
                    Log.i(TAG, "hue from red to blue in case of good concentration");
                    hue = 46920;
                    Log.i(TAG, "hue is(good concentration): "+ hue);
                    params.put("hue", hue);
                    jsonObject = new JSONObject(params);
                    sendRequest();
                }

            }

            //TODO: which number represents the best engagement?
            /**case 2: not concentrated enough*/
            if (0.3 <= engagementAverage && engagementAverage <= 0.5) {

                //TODO: maybe add some time measuremnet hier, if the person be hier more than 5 minutes then add orange?
                Log.i(TAG, "not enough concentrated");

                //TODO: If saturation is above 250? add some orange?
                if (sat < 260) {
                    sat += 10;
                    Log.i(TAG, "sat is: "+ sat);
                    params.put("sat", sat);
                    jsonObject = new JSONObject(params);
                    sendRequest();
                }

                if (hue < 46920) {
                    //increase hue gradually to bring the person back to focus
                    hue += 500;
                    Log.i(TAG, "hue is(not enough): "+ hue);
                    params.put("hue",hue);
                    jsonObject = new JSONObject(params);
                    sendRequest();
                }

                //TODO:in case hue is not blue anymore: do we want to add some orange also hier?
                if (hue > 46920) {
                    hue = 46920;
                    params.put("hue", hue);
                    Log.i(TAG, "hue is(not enough): "+ hue);
                    jsonObject = new JSONObject(params);
                    sendRequest();
                }
            }

            /**very poor concentration
             *
             *
             */
            if (engagementAverage <= 0.2) {
                Log.i(TAG, "very poor concentration");

                //TODO:Should I here change the hue to light red at the beginning instead of increasing it
                if (hue < 65535) {
                    //change the hue and saturation both to bring back to focus
                    hue += 20000;
                    params.put("hue", hue);
                    Log.i(TAG, "hue is(very poor): "+ hue);
                    jsonObject = new JSONObject(params);
                    sendRequest();
                }

                if (sat > 170) {
                    sat = 170;
                    params.put("sat", sat);
                    jsonObject = new JSONObject(params);
                    sendRequest();
                }

                if (sat < 170) {
                    sat += 10;
                    params.put("sat", sat);
                    jsonObject = new JSONObject();
                    sendRequest();
                }
            }
        }
    }


        public void sendRequest() {

            Log.i(TAG, "sendRequest is called");

            RequestQueue queue = Volley.newRequestQueue(this);

            JsonArrayRequest jsonArrReq = new JsonArrayRequest(Request.Method.PUT, url, jsonObject, new Response.Listener<JSONArray>() {


                @Override
                public void onResponse(JSONArray response) {
                    Log.i("JSONPost", response.toString());


                }

            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    Log.i("JSONPost", "Error:" + error.getMessage());

                }
            });

            queue.add(jsonArrReq);

        }


    protected void onPause() {
        super.onPause();
        // It is important to call stopListening when the Activity is paused
        // to avoid a resource leak from the LibMuse library.
        manager.stopListening();
    }

    public boolean isBluetoothEnabled() {
        return BluetoothAdapter.getDefaultAdapter().isEnabled();
    }

    @Override
    public void onClick(View v) {

        if (v.getId() == R.id.refresh) {
            // The user has pressed the "Refresh" button.
            // Start listening for nearby or paired Muse headbands. We call stopListening
            // first to make sure startListening will clear the list of headbands and start fresh.
            manager.stopListening();
            manager.startListening();

        } else if (v.getId() == R.id.connect) {


            // The user has pressed the "Connect" button to connect to
            // the headband in the spinner.

            // Listening is an expensive operation, so now that we know
            // which headband the user wants to connect to we can stop
            // listening for other headbands.
            manager.stopListening();

            List<Muse> availableMuses = manager.getMuses();
            Spinner musesSpinner = (Spinner) findViewById(R.id.muses_spinner);

            // Check that we actually have something to connect to.
            if (availableMuses.size() < 1 || musesSpinner.getAdapter().getCount() < 1) {
                Log.w(TAG, "There is nothing to connect to");
            } else {

                // Cache the Muse that the user has selected.
                muse = availableMuses.get(musesSpinner.getSelectedItemPosition());
                // Unregister all prior listeners and register our data listener to
                // receive the MuseDataPacketTypes we are interested in.  If you do
                // not register a listener for a particular data type, you will not
                // receive data packets of that type.
                muse.unregisterAllListeners();
                muse.registerConnectionListener(connectionListener);
                muse.registerDataListener(dataListener, MuseDataPacketType.EEG);
                muse.registerDataListener(dataListener, MuseDataPacketType.ALPHA_RELATIVE);
                muse.registerDataListener(dataListener, MuseDataPacketType.BETA_RELATIVE);
                muse.registerDataListener(dataListener, MuseDataPacketType.THETA_RELATIVE);
                muse.registerDataListener(dataListener, MuseDataPacketType.ACCELEROMETER);
                muse.registerDataListener(dataListener, MuseDataPacketType.BATTERY);
                muse.registerDataListener(dataListener, MuseDataPacketType.DRL_REF);
                muse.registerDataListener(dataListener, MuseDataPacketType.QUANTIZATION);
                muse.registerDataListener(dataListener, MuseDataPacketType.ALPHA_ABSOLUTE);
                muse.registerDataListener(dataListener, MuseDataPacketType.BETA_ABSOLUTE);
                muse.registerDataListener(dataListener, MuseDataPacketType.THETA_ABSOLUTE);
                muse.registerDataListener(dataListener, MuseDataPacketType.HSI_PRECISION);
                muse.registerDataListener(dataListener, MuseDataPacketType.IS_GOOD);


                //TO-DO: register ALPHA_..._SCORES


                // Initiate a connection to the headband and stream the data asynchronously.
                muse.runAsynchronously();
            }

        } else if (v.getId() == R.id.disconnect) {

            // The user has pressed the "Disconnect" button.
            // Disconnect from the selected Muse.
            if (muse != null) {
                muse.disconnect();
            }

        } else if (v.getId() == R.id.pause) {

            // The user has pressed the "Pause/Resume" button to either pause or
            // resume data transmission.  Toggle the state and pause or resume the
            // transmission on the headband.
            if (muse != null) {
                dataTransmission = !dataTransmission;
                muse.enableDataTransmission(dataTransmission);
            }
        }
    }

    //--------------------------------------
    // Permissions

    /**
     * The ACCESS_COARSE_LOCATION permission is required to use the
     * Bluetooth Low Energy library and must be requested at runtime for Android 6.0+
     * On an Android 6.0 device, the following code will display 2 dialogs,
     * one to provide context and the second to request the permission.
     * On an Android device running an earlier version, nothing is displayed
     * as the permission is granted from the manifest.
     * <p>
     * If the permission is not granted, then Muse 2016 (MU-02) headbands will
     * not be discovered and a SecurityException will be thrown.
     */
    private void ensurePermissions() {

        if (ContextCompat.checkSelfPermission(this,
                Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            // We don't have the ACCESS_COARSE_LOCATION permission so create the dialogs asking
            // the user to grant us the permission.

            DialogInterface.OnClickListener buttonListener =
                    new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int which) {
                            dialog.dismiss();
                            ActivityCompat.requestPermissions(MainActivity.this,
                                    new String[]{Manifest.permission.ACCESS_COARSE_LOCATION},
                                    0);
                        }
                    };

            // This is the context dialog which explains to the user the reason we are requesting
            // this permission.  When the user presses the positive (I Understand) button, the
            // standard Android permission dialog will be displayed (as defined in the button
            // listener above).
            AlertDialog introDialog = new AlertDialog.Builder(this)
                    .setTitle(R.string.permission_dialog_title)
                    .setMessage(R.string.permission_dialog_description)
                    .setPositiveButton(R.string.permission_dialog_understand, buttonListener)
                    .create();
            introDialog.show();
        }
    }


    //--------------------------------------
    // Listeners

    /**
     * You will receive a callback to this method each time a headband is discovered.
     * In this example, we update the spinner with the MAC address of the headband.
     */
    public void museListChanged() {
        final List<Muse> list = manager.getMuses();
        spinnerAdapter.clear();
        for (Muse m : list) {
            spinnerAdapter.add(m.getName() + " - " + m.getMacAddress());
        }

    }

    /**
     * You will receive a callback to this method each time there is a change to the
     * connection state of one of the headbands.
     *
     * @param p    A packet containing the current and prior connection states
     * @param muse The headband whose state changed.
     */
    public void receiveMuseConnectionPacket(final MuseConnectionPacket p, final Muse muse) {

        final ConnectionState current = p.getCurrentConnectionState();

        // Format a message to show the change of connection state in the UI.
        final String status = p.getPreviousConnectionState() + " -> " + current;
        Log.i(TAG, status);

        // Update the UI with the change in connection state.
        handler.post(new Runnable() {
            @Override
            public void run() {

                final TextView statusText = (TextView) findViewById(R.id.con_status);
                statusText.setText(status);

                final MuseVersion museVersion = muse.getMuseVersion();
                final TextView museVersionText = (TextView) findViewById(R.id.version);
                // If we haven't yet connected to the headband, the version information
                // will be null.  You have to connect to the headband before either the
                // MuseVersion or MuseConfiguration information is known.
                if (museVersion != null) {
                    final String version = museVersion.getFirmwareType() + " - "
                            + museVersion.getFirmwareVersion() + " - "
                            + museVersion.getProtocolVersion();
                    museVersionText.setText(version);
                } else {
                    museVersionText.setText(R.string.undefined);
                }
            }
        });

        if (current == ConnectionState.DISCONNECTED) {
            Log.i(TAG, "Muse disconnected:" + muse.getName());
            // Save the data file once streaming has stopped.
            saveFile();
            // We have disconnected from the headband, so set our cached copy to null.
            this.muse = null;

        }

    }

    /**
     * You will receive a callback to this method each time the headband sends a MuseDataPacket
     * that you have registered.  You can use different listeners for different packet types or
     * a single listener for all packet types as we have done here.
     *
     * @param p    The data packet containing the data from the headband (eg. EEG data)
     * @param muse The headband that sent the information.
     */
    public void receiveMuseDataPacket(final MuseDataPacket p, final Muse muse) {
        //writeDataPacketToFile(p);

        // TODO → How this packages receive the data

        //a limit to initialize the value with
        int limit = 0;

        // valuesSize returns the number of data values contained in the packet.
        final long n = p.valuesSize();
        //Test the value size n
        System.out.print(n);

        String dataString = "";
        String values = "";


        if (alphaBuffer.length > 0 && betaBuffer.length > 0 && thetaBuffer.length > 0) {
            //changeTheLight();
        }
        switch (p.packetType()) {
            /**case EEG:
             assert (eegBuffer.length >= n);
             values = getEegChannelValues(eegBuffer, p);
             dataString += "eeg_raw," + p.timestamp()+",";
             dataString += values;
             eegStale = true;
             break; **/
            case ACCELEROMETER:
                assert (accelBuffer.length >= n);
                getAccelValues(p);
                accelStale = true;
                break;
            case ALPHA_RELATIVE:
                assert (alphaBuffer.length >= n);
                Log.i(TAG, "timestamp for alpha_relative: " + p.timestamp());
                values = getEegChannelValues(alphaBuffer, p);
                changeTheLight();
                dataString += "alpha_relative," + p.timestamp() + ",";
                dataString += values;
                alphaStale = true;
                break;
            case BETA_RELATIVE:
                assert (betaBuffer.length >= n);
                Log.i(TAG, "timestamp for beta_relative: " + p.timestamp());
                values = getEegChannelValues(betaBuffer, p);
                changeTheLight();
                dataString += "beta_relative," + p.timestamp() + ",";
                dataString += values;
                betaStale = true;
                break;

            case THETA_RELATIVE:
                assert (thetaBuffer.length >= n);
                Log.i(TAG, "timestamp for theta_relative: " + p.timestamp());
                values = getEegChannelValues(alphaBuffer, p);
                changeTheLight();
                dataString += "theta_relative," + p.timestamp() + ",";
                dataString += values;
                thetaStale = true;
                break;

            case ALPHA_ABSOLUTE:
                assert (alphaAbsoluteBuffer.length >= n);
                Log.i(TAG, "timestamp for alpha_absolute: " + p.timestamp());
                values = getEegChannelValues(alphaAbsoluteBuffer, p);
                dataString += "alpha_absolute," + p.timestamp() + ",";
                dataString += values;
                alphaAbsoluteStale = true;
                break;

            case BETA_ABSOLUTE:
                assert (betaAbsoluteBuffer.length >= n);
                Log.i(TAG, "timestamp for beta_absolute: " + p.timestamp());
                values = getEegChannelValues(betaAbsoluteBuffer, p);
                dataString += "beta_absolute," + p.timestamp() + ",";
                dataString += values;
                betaAbsolsulteStale = true;
                break;


            case THETA_ABSOLUTE:
                assert (thetaAbsoluteBuffer.length >= n);
                Log.i(TAG, "timestamp for theta_absolute: " + p.timestamp());
                values = getEegChannelValues(thetaAbsoluteBuffer, p);
                dataString += "theta_absolute," + p.timestamp() + ",";
                dataString += values;
                thetaAbsolsulteStale = true;
                break;


            case HSI_PRECISION:
                assert (hci_precision.length >= n);
                values = getEegQualityValue(hci_precision, p);
                Log.i(TAG, "quality_Report:");
                dataString += "quality," + p.timestamp() + ",";
                dataString += values;
                break;

            case IS_GOOD:
                assert (isGood.length >= n);
                values = eegIsGood(isGood, p);
                Log.i(TAG, "is good:");
                dataString += "isGood," + p.timestamp() + ",";
                dataString += values;
                break;


            case EEG:
            case BATTERY:
            case DRL_REF:
            case QUANTIZATION:
            default:
                break;
        }

        if (dataString != "") {
            writeDataPacketToFile(dataString + "\n");
        }

        Log.i(TAG, "muse_data is written");
    }

    /**
     * You will receive a callback to this method each time an artifact packet is generated if you
     * have registered for the ARTIFACTS data type.  MuseArtifactPackets are generated when
     * eye blinks are detected, the jaw is clenched and when the headband is put on or removed.
     *
     * @param p    The artifact packet with the data from the headband.
     * @param muse The headband that sent the information.
     */
    public void receiveMuseArtifactPacket(final MuseArtifactPacket p, final Muse muse) {
    }

    /**
     * Helper methods to get different packet values.  These methods simply store the
     * data in the buffers for later display in the UI.
     * <p>
     * getEegChannelValue can be used for any EEG or EEG derived data packet type
     * such as EEG, ALPHA_ABSOLUTE, ALPHA_RELATIVE or HSI_PRECISION.  See the documentation
     * of MuseDataPacketType for all of the available values.
     * Specific packet types like ACCELEROMETER, GYRO, BATTERY and DRL_REF have their own
     * getValue methods.
     */
    private String getEegChannelValues(double[] buffer, MuseDataPacket p) {

        buffer[0] = p.getEegChannelValue(Eeg.EEG1);
        buffer[1] = p.getEegChannelValue(Eeg.EEG2);
        buffer[2] = p.getEegChannelValue(Eeg.EEG3);
        buffer[3] = p.getEegChannelValue(Eeg.EEG4);
        buffer[4] = p.getEegChannelValue(Eeg.AUX_LEFT);
        buffer[5] = p.getEegChannelValue(Eeg.AUX_RIGHT);

        Log.i(TAG, "buffer 0: " + buffer[0]);
        Log.i(TAG, "buffer 1: " + buffer[1]);
        Log.i(TAG, "buffer 2: " + buffer[2]);
        Log.i(TAG, "buffer 3: " + buffer[3]);
        Log.i(TAG, "buffer 4: " + buffer[4]);
        Log.i(TAG, "buffer 5: " + buffer[5]);


        return buffer[0] + "," + buffer[1] + "," + buffer[2] + "," + buffer[3];

    }

    private String getEegQualityValue(double[] hci_buffer, MuseDataPacket p) {
        hci_buffer[0] = p.getEegChannelValue(Eeg.EEG1);
        hci_buffer[1] = p.getEegChannelValue(Eeg.EEG2);
        hci_buffer[2] = p.getEegChannelValue(Eeg.EEG3);
        hci_buffer[3] = p.getEegChannelValue(Eeg.EEG4);

        Log.i(TAG, "buffer 0: " + hci_buffer[0]);
        Log.i(TAG, "buffer 1: " + hci_buffer[1]);
        Log.i(TAG, "buffer 2: " + hci_buffer[2]);
        Log.i(TAG, "buffer 3: " + hci_buffer[3]);

        return hci_buffer[0] + "," + hci_buffer[1] + "," + hci_buffer[2] + "," + hci_buffer[3];

    }


    private String eegIsGood(double[] isGoodBuffer, MuseDataPacket p) {
        isGoodBuffer[0] = p.getEegChannelValue(Eeg.EEG1);
        isGoodBuffer[1] = p.getEegChannelValue(Eeg.EEG2);
        isGoodBuffer[2] = p.getEegChannelValue(Eeg.EEG3);
        isGoodBuffer[3] = p.getEegChannelValue(Eeg.EEG4);

        return isGoodBuffer[0] + "," + isGoodBuffer[1] + "," + isGoodBuffer[2] + "," + isGoodBuffer[3];
    }

    private void getAccelValues(MuseDataPacket p) {
        accelBuffer[0] = p.getAccelerometerValue(Accelerometer.X);
        accelBuffer[1] = p.getAccelerometerValue(Accelerometer.Y);
        accelBuffer[2] = p.getAccelerometerValue(Accelerometer.Z);
    }


    //--------------------------------------
    // UI Specific methods

    /**
     * Initializes the UI of the example application.
     */
    private void initUI() {
        setContentView(R.layout.activity_main);
        Button refreshButton = (Button) findViewById(R.id.refresh);
        refreshButton.setOnClickListener(this);
        Button connectButton = (Button) findViewById(R.id.connect);
        connectButton.setOnClickListener(this);
        Button disconnectButton = (Button) findViewById(R.id.disconnect);
        disconnectButton.setOnClickListener(this);
        Button pauseButton = (Button) findViewById(R.id.pause);
        pauseButton.setOnClickListener(this);

        spinnerAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item);
        Spinner musesSpinner = (Spinner) findViewById(R.id.muses_spinner);
        musesSpinner.setAdapter(spinnerAdapter);
    }

    /**
     * The runnable that is used to update the UI at 60Hz.
     * <p>
     * We update the UI from this Runnable instead of in packet handlers
     * because packets come in at high frequency -- 220Hz or more for raw EEG
     * -- and it only makes sense to update the UI at about 60fps. The update
     * functions do some string allocation, so this reduces our memory
     * footprint and makes GC pauses less frequent/noticeable.
     */
    private final Runnable tickUi = new Runnable() {
        @Override
        public void run() {
            if (eegStale) {
                updateEeg();
            }
            if (accelStale) {
                updateAccel();
            }
            if (alphaStale) {
                updateAlpha();
            }
            handler.postDelayed(tickUi, 1000 / 60);
        }
    };

    /**
     * The following methods update the TextViews in the UI with the data
     * from the buffers.
     */


    //here us to change views in the app
    private void updateAccel() {
        TextView acc_x = (TextView) findViewById(R.id.acc_x);
        TextView acc_y = (TextView) findViewById(R.id.acc_y);
        TextView acc_z = (TextView) findViewById(R.id.acc_z);
        acc_x.setText(String.format("%6.2f", accelBuffer[0]));
        acc_y.setText(String.format("%6.2f", accelBuffer[1]));
        acc_z.setText(String.format("%6.2f", accelBuffer[2]));
    }

    private void updateEeg() {
        TextView tp9 = (TextView) findViewById(R.id.eeg_tp9);
        TextView fp1 = (TextView) findViewById(R.id.eeg_af7);
        TextView fp2 = (TextView) findViewById(R.id.eeg_af8);
        TextView tp10 = (TextView) findViewById(R.id.eeg_tp10);
        tp9.setText(String.format("%6.2f", eegBuffer[0]));
        fp1.setText(String.format("%6.2f", eegBuffer[1]));
        fp2.setText(String.format("%6.2f", eegBuffer[2]));
        tp10.setText(String.format("%6.2f", eegBuffer[3]));
    }

    private void updateAlpha() {
        TextView elem1 = (TextView) findViewById(R.id.elem1);
        elem1.setText(String.format("%6.2f", alphaBuffer[0]));
        TextView elem2 = (TextView) findViewById(R.id.elem2);
        elem2.setText(String.format("%6.2f", alphaBuffer[1]));
        TextView elem3 = (TextView) findViewById(R.id.elem3);
        elem3.setText(String.format("%6.2f", alphaBuffer[2]));
        TextView elem4 = (TextView) findViewById(R.id.elem4);
        elem4.setText(String.format("%6.2f", alphaBuffer[3]));
    }


    //--------------------------------------
    // File I/O


    /**
     * We don't want to block the UI thread while we write to a file, so the file
     * writing is moved to a separate thread.
     */
    private final Thread fileThread = new Thread() {
        @Override
        public void run() {
            Looper.prepare();
            fileHandler.set(new Handler());
            //final File dir = getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS);
            File dir = new File("//sdcard//Download//");
            final File file = new File(dir, "muse_data.txt");
            final File file2 = new File(dir, "quality_report.txt");
            try {
                file.createNewFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
            // MuseFileWriter will append to an existing file.
            // In this case, we want to start fresh so the file
            // if it exists.
            if (file.exists()) {
                file.delete();
            }

            if (file2.exists()) {
                file.delete();
            }

            Log.i(TAG, "Writing data to: " + file.getAbsolutePath());
            //fileWriter.set(MuseFileFactory.getMuseFileWriter(file));
            OutputStreamWriter fos = null;
            FileOutputStream fOut = null;
            try {
                fOut = new FileOutputStream(file);
                fos = new OutputStreamWriter(fOut);

            } catch (IOException e) {
                e.printStackTrace();
                Log.i(TAG, "muse_data is not open");
            }
            Log.i(TAG, "muse_data is open and written to:");
            fileWriter.set(fos);
            fileWriter2.set(fOut);
            writeDataPacketToFile("data_type,timestamp,EEG1,EEG2,EEG3,EEG4\n");
            Looper.loop();
        }
    };

    /**
     * Writes the provided MuseDataPacket to the file.  MuseFileWriter knows
     * how to write all packet types generated from LibMuse.
     *
     * @param p The data packet to write.
     */
    private void writeDataPacketToFile(final MuseDataPacket p) {
        Handler h = fileHandler.get();
        if (h != null) {
            h.post(new Runnable() {
                @Override
                public void run() {
                    //fileWriter.get().addDataPacket(0, p);
                }
            });
        }
    }

    private void writeDataPacketToFile(final String s) {
        Handler h = fileHandler.get();
        if (h != null) {
            h.post(new Runnable() {
                @Override
                public void run() {
                    try {
                        FileOutputStream w = fileWriter2.get();
                        OutputStreamWriter w2 = fileWriter.get();
                        w2.write(s);
                        w.flush();
                        w2.flush();
                        Log.i(TAG, "data is written to the file");
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            });
        }
    }

    /**
     * Flushes all the data to the file and closes the file writer.
     */
    private void saveFile() {
        Handler h = fileHandler.get();
        if (h != null) {
            h.post(new Runnable() {
                @Override
                public void run() {
                    OutputStreamWriter w = fileWriter.get();
                    FileOutputStream w2 = fileWriter2.get();
                    // Annotation strings can be added to the file to
                    // give context as to what is happening at that point in
                    // time.  An annotation can be an arbitrary string or
                    // may include additional AnnotationData.
                    //w.addAnnotationString(0, "Disconnected");
                    //w.flush();
                    //w.close();
                    if (w != null && w2 != null) {
                        try {
                            w.flush();
                            w2.flush();
                            w.close();
                            w2.close();
                        } catch (IOException e) {
                            e.printStackTrace();
                            Log.i(TAG, "muse_data is not closed");
                        }
                        Log.i(TAG, "muse_data is closed");
                    }

                }
            });
        }
    }

    /**
     * Reads the provided .muse file and prints the data to the logcat.
     *
     * @param name The name of the file to read.  The file in this example
     *             is assumed to be in the Environment.DIRECTORY_DOWNLOADS
     *             directory.
     */
    private void playMuseFile(String name) throws IOException {

        File dir = getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS);
        File file = new File(dir, name);

        final String tag = "Muse File Reader";

        if (!file.exists()) {
            Log.w(tag, "file doesn't exist");
            return;
        }

        MuseFileReader fileReader = MuseFileFactory.getMuseFileReader(file);

        // Loop through each message in the file.  gotoNextMessage will read the next message
        // and return the result of the read operation as a Result.
        Result res = fileReader.gotoNextMessage();
        while (res.getLevel() == ResultLevel.R_INFO && !res.getInfo().contains("EOF")) {

            MessageType type = fileReader.getMessageType();
            int id = fileReader.getMessageId();
            long timestamp = fileReader.getMessageTimestamp();


            Log.i(tag, "type: " + type.toString() +
                    " id: " + Integer.toString(id) +
                    " timestamp: " + String.valueOf(timestamp));

            switch (type) {
                // EEG messages contain raw EEG data or DRL/REF data.
                // EEG derived packets like ALPHA_RELATIVE and artifact packets
                // are stored as MUSE_ELEMENTS messages.
                case EEG:
                case BATTERY:
                case ACCELEROMETER:
                case QUANTIZATION:
                case GYRO:
                case MUSE_ELEMENTS:
                    MuseDataPacket packet = fileReader.getDataPacket();
                    Log.i(tag, "data packet: " + packet.packetType().toString());
                    break;
                case VERSION:
                    MuseVersion version = fileReader.getVersion();
                    Log.i(tag, "version" + version.getFirmwareType());
                    break;
                case CONFIGURATION:
                    MuseConfiguration config = fileReader.getConfiguration();
                    Log.i(tag, "config" + config.getBluetoothMac());
                    break;
                case ANNOTATION:
                    AnnotationData annotation = fileReader.getAnnotation();
                    Log.i(tag, "annotation" + annotation.getData());
                    break;
                default:
                    break;
            }

            // Read the next message.
            res = fileReader.gotoNextMessage();
        }
    }

    //--------------------------------------
    // Listener translators
    //
    // Each of these classes extend from the appropriate listener and contain a weak reference
    // to the activity.  Each class simply forwards the messages it receives back to the Activity.
    class MuseL extends MuseListener {
        final WeakReference<MainActivity> activityRef;

        MuseL(final WeakReference<MainActivity> activityRef) {
            this.activityRef = activityRef;
        }

        @Override
        public void museListChanged() {
            activityRef.get().museListChanged();
        }
    }

    class ConnectionListener extends MuseConnectionListener {
        final WeakReference<MainActivity> activityRef;

        ConnectionListener(final WeakReference<MainActivity> activityRef) {
            this.activityRef = activityRef;
        }

        @Override
        public void receiveMuseConnectionPacket(final MuseConnectionPacket p, final Muse muse) {
            activityRef.get().receiveMuseConnectionPacket(p, muse);
        }
    }

    class DataListener extends MuseDataListener {
        final WeakReference<MainActivity> activityRef;

        DataListener(final WeakReference<MainActivity> activityRef) {
            this.activityRef = activityRef;
        }

        @Override
        public void receiveMuseDataPacket(final MuseDataPacket p, final Muse muse) {
            activityRef.get().receiveMuseDataPacket(p, muse);
            //activityRef.get().receiveQualityReport(p, muse);
        }

        @Override
        public void receiveMuseArtifactPacket(final MuseArtifactPacket p, final Muse muse) {
            activityRef.get().receiveMuseArtifactPacket(p, muse);
        }
    }
}
