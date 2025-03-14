import 'package:flutter/material.dart';

class Calculadora extends StatefulWidget {
  const Calculadora({super.key});

  @override
  _CalculadoraState createState() => _CalculadoraState();
}

class _CalculadoraState extends State<Calculadora> {
  final TextEditingController _controller1 = TextEditingController();
  final TextEditingController _controller2 = TextEditingController();
  String _resultadoSoma = '';
  String _resultadoSub = '';


  void _somar() {
    final num1 = double.tryParse(_controller1.text);
    final num2 = double.tryParse(_controller2.text);

    if (num1 != null && num2 != null) {
      setState(() {
        _resultadoSoma = (num1 + num2).toString();
      });
    } else {
      setState(() {
        _resultadoSoma = 'Valor inválido.';
      });
    }
  }

  void _subtrair() {
    final num1 = double.tryParse(_controller1.text);
    final num2 = double.tryParse(_controller2.text);


    if (num1 != null && num2 != null) {
      setState(() {
        _resultadoSub = (num1 - num2).toString();
      });
    } else {
      setState(() {
        _resultadoSub = 'Valor inválido.';
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
          title: Text('Calculadora'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              TextField(
                controller: _controller1,
                decoration: InputDecoration(
                  labelText: 'Número 1:'
                ),
              ),
              TextField(
                controller: _controller2,
                decoration: InputDecoration(
                  labelText: 'Número 2:'
                ),
              ),
              SizedBox(
                height: 32,
              ),
              FilledButton(onPressed: _somar, child: Text('Somar')),
              FilledButton(onPressed: _subtrair, child: Text('Subtrair')),
              TextField(
                decoration: InputDecoration(
                  labelText: 'Resultado da soma'
                ),
                readOnly: true,
                controller: TextEditingController(text: _resultadoSoma),
              ),
              TextField(
                decoration: InputDecoration(
                  labelText: 'Resultado da Subtração'
                ),
                readOnly: true,
                controller: TextEditingController(text: _resultadoSub),
              )
            ],
          ),
          ),
      ),
    );
  }
}
