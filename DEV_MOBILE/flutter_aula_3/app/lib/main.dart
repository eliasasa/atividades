import 'package:flutter/material.dart';
import 'package:app/components/user_profile.dart';
import 'package:app/components/mod_button.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
          ProfileInfo(nome: 'Elias',url: 'https://th.bing.com/th/id/R.8d2d0c9be78349cece3d1fe6fe1b2777?rik=ZMHnDP%2bT0cKzNA&pid=ImgRaw&r=0',),
          ModButton(nome: 'aperte aqui',)
        ],)
      ),
    );
    
    }
  }