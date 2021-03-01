package com.example.elvisapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class VollyActivity extends AppCompatActivity {
    EditText cajaId, cajaNombre, cajaDireccion;
    Button botonGuardar, botonBuscar;
    TextView datos;
    RecyclerView recyclerViewAlumno;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_volly);
    }

    private void cargarDatos(){
        cajaId = findViewById(R.id.txtIdAlumnoVolly);
        cajaNombre = findViewById(R.id.txtNombreAlumnoVolly);
        cajaDireccion = findViewById(R.id.txtDireccionAlumnoVolly);
        botonGuardar = findViewById(R.id.btnInsertarVolly);
        botonBuscar = findViewById(R.id.btnBuscarVolly);
        datos = findViewById(R.id.lblDAtosAlumnoVolly);
    }
}