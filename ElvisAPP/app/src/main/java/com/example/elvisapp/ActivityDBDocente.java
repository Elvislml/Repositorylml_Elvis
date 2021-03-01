package com.example.elvisapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class ActivityDBDocente extends AppCompatActivity implements View.OnClickListener{

    EditText cajaCedula, cajaNombre, cajaApellidos;
    Button btnGuardar, btnModifcar, btnEliminarTodo, btnEliminarCedula;
    TextView datos;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_d_b_docente);

        cajaCedula = findViewById(R.id.txtCedulaHelper);
        cajaApellidos = findViewById(R.id.txtApellidosHelper);
        cajaNombre = findViewById(R.id.txtNombresHelper);
        btnGuardar = findViewById(R.id.btnGuardasH);
        btnModifcar = findViewById(R.id.btnModificarH);
        btnEliminarTodo = findViewById(R.id.btnEliminarTodoH);
        btnEliminarCedula = findViewById(R.id.btnEliminarCedulaH);
        datos = findViewById(R.id.lbldatosHelper);

        btnGuardar.setOnClickListener(this);
        btnModifcar.setOnClickListener(this);
        btnEliminarTodo.setOnClickListener(this);
        btnEliminarCedula.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()){
            case R.id.btnGuardasH:

        }

    }
}