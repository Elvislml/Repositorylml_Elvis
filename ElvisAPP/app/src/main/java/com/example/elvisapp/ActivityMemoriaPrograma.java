package com.example.elvisapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

public class ActivityMemoriaPrograma extends AppCompatActivity {
    Button boton;
    TextView datos;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_memoria_programa);

        datos = findViewById(R.id.lblDatosAP);
        boton = findViewById(R.id.btnLeerAP);
        boton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    InputStream input = getResources().openRawResource(R.raw.archivo_raw);
                    BufferedReader lector = new BufferedReader(new InputStreamReader(input));
                    String informacion = lector.readLine();
                    datos.setText(informacion);
                    lector.close();
                }catch (Exception ex){
                    Log.e("Error de Lectura", ex.getMessage());
                }
            }
        });
    }
}