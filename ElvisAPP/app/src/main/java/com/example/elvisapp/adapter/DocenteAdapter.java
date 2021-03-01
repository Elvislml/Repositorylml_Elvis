package com.example.elvisapp.adapter;


import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class DocenteAdapter extends RecyclerView.Adapter<DocenteAdapter.ViewHolderDocente> implements View.OnClickListener{

    List<DocenteAdapter> listaDocent;

    @NonNull
    @Override
    public ViewHolderDocente onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return null;
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolderDocente holder, int position) {

    }

    @Override
    public int getItemCount() {
        return 0;
    }

    @Override
    public void onClick(View view) {

    }


    public static  class ViewHolderDocente extends RecyclerView.ViewHolder{

        public ViewHolderDocente(View itemView) {
            super(itemView);
        }
    }



}

