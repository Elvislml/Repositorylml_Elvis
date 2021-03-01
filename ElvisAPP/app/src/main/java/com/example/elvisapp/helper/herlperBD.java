package com.example.elvisapp.helper;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class herlperBD extends SQLiteOpenHelper {

    public herlperBD(Context context, String name, SQLiteDatabase.CursorFactory factory, int version) {
        super(context, name, factory, version);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE docente(id INTEGER PRIMARY KEY AUTOINCREMENT, cedula TEXT, apellido TEXT, nombre TEXT)");

    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int i, int i1) {

    }

    public void insertar(String cedula, String apellido, String nombre){
        ContentValues valores = new ContentValues();
        valores.put("cedula", cedula);
        valores.put("apellido", apellido);
        valores.put("nombre", nombre);

        this.getWritableDatabase().insert("docente", null, valores);

    }

    public void modificar(String cedula , String apellido,String nombre){
        ContentValues valores = new ContentValues();
        valores.put("apellido", apellido);
        valores.put("nombres", nombre);
        this.getWritableDatabase().update("docente", valores, "cedula'"+cedula+"'", null);
    }

    public void eliminarTodos (){
        this.getReadableDatabase().delete("docente",null,null);
    }

    public void eliminarCedula(String cedula){
        this.getReadableDatabase().delete("docente","cedula='"+cedula+"'",null);
    }

    public String leerTodos(){
        String consult ="";
        Cursor cursor = this.getReadableDatabase().rawQuery("SELECT * FROM docente",null);
        if (cursor.moveToFirst()){
            do {
                String cedula = cursor.getString(cursor.getColumnIndex("cedula"));
                String apellido = cursor.getString(cursor.getColumnIndex("apellido"));
                String nombre = cursor.getString(cursor.getColumnIndex("nombre"));
                consult+=cedula+" " + apellido +" " + nombre;
            }while (cursor.moveToNext());
        }
        return consult;
    }

    public String leerCedula(String ced){
        String consult ="";
        Cursor cursor = this.getReadableDatabase().rawQuery("SELECT * FROM docente WHERE cedula ='"+ced+"'",null);
        if (cursor.moveToFirst()){
            do {
                String cedula = cursor.getString(cursor.getColumnIndex("cedula"));
                String apellido = cursor.getString(cursor.getColumnIndex("apellido"));
                String nombre = cursor.getString(cursor.getColumnIndex("nombre"));
                consult+=cedula+" " + apellido +" " + nombre;
            }while (cursor.moveToNext());
        }
        return consult;
    }
}
