package com.example.elvisapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Dialog;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.elvisapp.ui.login.LoginActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button boton = findViewById(R.id.btnIngresar);
        final EditText cajaNombres = findViewById(R.id.txtNombres);
        final EditText cajaApellidos =  findViewById(R.id.txtApellidos);


        boton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, ActivityNombres.class);
                Bundle bundle = new Bundle();
                bundle.putString("Nombre", cajaNombres.getText().toString());
                bundle.putString("Apellidos", cajaApellidos.getText().toString());
                intent.putExtras(bundle);
                startActivity(intent);
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        Intent intent;
        switch (item.getItemId()){
            case R.id.opcionLogin :
                intent = new Intent(MainActivity.this, LoginActivity.class);
                startActivity(intent);
                break;

            case R.id.opcionParametros:
                intent = new Intent(MainActivity.this, ActividadFragmentos.class);
                startActivity(intent);
                break;
            case R.id.opcionDialogo:
                Dialog dialogoLogin = new Dialog( MainActivity.this);
                dialogoLogin.setContentView(R.layout.dlg_login);

                final EditText cajaUsuario = dialogoLogin.findViewById(R.id.txtUsuarioDlg);
                final EditText cajaClave = dialogoLogin.findViewById(R.id.txtClaveDlg);
                Button botonDlg = dialogoLogin.findViewById(R.id.btnIngresarDlg);

                botonDlg.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        Toast.makeText(MainActivity.this,
                                cajaUsuario.getText().toString() + " " +
                                        cajaClave.getText().toString(),
                                Toast.LENGTH_SHORT).show();
                    }
                });


                dialogoLogin.show();
            default:
                return super.onOptionsItemSelected(item);
        }
        return true;
    }
}



















