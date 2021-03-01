package com.example.elvisapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class ActivityNombres extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_nombres);
        TextView txtNombre = findViewById(R.id.lblNombres);
        TextView txtApellidos = findViewById(R.id.lblApellidos);

        Bundle bundle = this.getIntent().getExtras();
        txtNombre.setText(bundle.getString("Nombre"));
        txtApellidos.setText(bundle.getString("Apellidos"));
    }
}