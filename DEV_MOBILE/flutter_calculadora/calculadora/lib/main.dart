import 'package:calculadora/pages/bicicleta.dart';
import 'package:flutter/material.dart';
import 'package:calculadora/pages/calculadora.dart';
import 'package:calculadora/pages/conversora.dart';
import 'package:calculadora/pages/taxi.dart';
import 'package:calculadora/pages/banco.dart';


void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      routes: {
        '/': (context) => HomeScreen(),
        '/pages/calculadora': (context) => Calculadora(),
        '/pages/conversora': (context) => Conversora(),
        '/pages/taxi': (context) => Taxi(),
        '/pages/banco': (context) => Banco(),
        '/pages/bicicleta': (context) => Bicicleta(),

      },
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Home'),
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: <Widget>[
            DrawerHeader(
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
              child: Text(
                'Menu',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 24,
                ),
              ),
            ),
            ListTile(
              leading: Icon(Icons.calculate),
              title: Text('Calculadora'),
              onTap: () {
                Navigator.pushNamed(context, '/pages/calculadora');
              },
            ),
            ListTile(
              leading: Icon(Icons.swap_horiz),
              title: Text('Conversora'),
              onTap: () {
                Navigator.pushNamed(context, '/pages/conversora');
              },
            ),
            ListTile(
              leading: Icon(Icons.monetization_on),
              title: Text('Poupança'),
              onTap: () {
                Navigator.pushNamed(context, '/pages/banco');
              },
            ),
            ListTile(
              leading: Icon(Icons.local_taxi),
              title: Text('Taxi'),
              onTap: () {
                Navigator.pushNamed(context, '/pages/taxi');
              },
            ),
            ListTile(
              leading: Icon(Icons.directions_bike_sharp),
              title: Text('Bicicletas'),
              onTap: () {
                Navigator.pushNamed(context, '/pages/bicicleta');
              },
            ),
          ],
        ),
      ),
      body: Center(
        child: Text('Bem-vindo à Tela Inicial!'),
      ),
    );
  }
}

