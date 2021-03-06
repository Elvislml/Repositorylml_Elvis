package com.example.elvisapp.controlador.swvolley;

import android.content.Context;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.example.elvisapp.modelo.Alumno;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;
import java.util.jar.JarException;

public class ServicioWebVolley {
    String host = "http://reneguaman.000webhostapp.com/";
    String insertar_url = "insertar_alumno.php";
    String GET = "obtener_alumnos.php";
    Context context;
    boolean estado;

    List<Alumno> listaAlumnos;

    public ServicioWebVolley (Context context){
        this.context = context;
        listaAlumnos = new ArrayList<Alumno>();
    }

    public boolean insert(Alumno alumno) throws JSONException {
        String url = host + insertar_url;
        JSONObject json = new JSONObject();
        json.put("nombre", alumno.getNombre());
        json.put("direccion",alumno.getDireccion());

        JsonObjectRequest request = new JsonObjectRequest(
                Request.Method.POST, url, json, new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                estado = true;
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                estado = false;
            }
        });
        VolleyAlumnosSingleton.getInstance(context).addToRequestQue(request);
        return false;
    }

    public String obtenerAlumno (){
        return "";
    }

}
