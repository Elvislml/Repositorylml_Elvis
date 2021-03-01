package com.example.elvisapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;

public class ActividadMemoriaInterna extends AppCompatActivity implements View.OnClickListener{

    EditText cajaCedula, cajaApellidos, cajaNombres;
    Button botonLeer,botonEscribir;
    TextView datos;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_actividad_memoria_interna);
        cajaCedula = findViewById(R.id.txtCedulaMI);
        cajaApellidos = findViewById(R.id.txtApellidosMI);
        cajaNombres = findViewById(R.id.txtNombresMI);
        botonLeer = findViewById(R.id.btnLeerMI);
        botonEscribir = findViewById(R.id.btnEscribirMI);
        botonEscribir.setOnClickListener(this);
        botonLeer.setOnClickListener(this);
        datos = findViewById(R.id.lblDatosMI);
    }
    @Override
    public void onClick(View v){
        switch (v.getId()){
            case R.id.btnEscribirMI:
                try {
                    OutputStreamWriter escritor = new OutputStreamWriter(
                            openFileOutput("archivo.txt", Context.MODE_APPEND));
                    escritor.write(cajaCedula.getText().toString() + " " +
                            cajaApellidos.getText().toString() + " " +
                            cajaNombres.getText().toString()+";");
                    escritor.close();
                }catch (Exception ex){
                    Log.e("error escritura", ex.getMessage());

                }break;
            case R.id.btnLeerMI:
                try{
                    BufferedReader lector = new BufferedReader(new InputStreamReader(
                            openFileInput("archivo.txt")));
                    String informacion = lector.readLine();
                    datos.setText(informacion);
                    lector.close();
                }catch (Exception ex){
                    Log.e("error Lectura", ex.getMessage());
                }
        }
    }
}