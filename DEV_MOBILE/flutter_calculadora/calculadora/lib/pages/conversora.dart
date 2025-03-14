import 'package:flutter/material.dart';

class Conversora extends StatefulWidget {
  const Conversora({super.key});

  @override
  _ConversoraState createState() => _ConversoraState();
}

class _ConversoraState extends State<Conversora> {
  final TextEditingController _controller1 = TextEditingController();
  String _resultadoConv = '';


  void _metrosCm() {
    final _metros = double.tryParse(_controller1.text);

    if (_metros != null) {
      setState(() {
        _resultadoConv = (_metros * 1000).toString() + ' cm';
      });
    } else {
      setState(() {
        _resultadoConv = 'Valor Inválido.';
      });
    }

    
  }
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: false,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text('Conversora'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              TextField(
                controller: _controller1,
                decoration: InputDecoration(
                  labelText: 'Valor em metros:'
                ),
              ),
              SizedBox(
                height: 32,
              ),
              FilledButton(onPressed: _metrosCm, child: Text('Converter')),
              TextField(
                decoration: InputDecoration(
                  labelText: 'Resultado da Conversão em centímetros'
                ),
                readOnly: true,
                controller: TextEditingController(text: _resultadoConv),
              ),
            ],
          ),
          ),
      ),
    );
  }
}
