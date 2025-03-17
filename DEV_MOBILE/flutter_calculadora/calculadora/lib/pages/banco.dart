import 'package:flutter/material.dart';

class Banco extends StatefulWidget {
  const Banco({super.key});

  @override
  _BancoState createState() => _BancoState();
}

class _BancoState extends State<Banco> {
  final TextEditingController _controller1 = TextEditingController();
  String _rendimento = '';


  void _poupanca() {
    final _deposito = double.tryParse(_controller1.text);

    if (_deposito != null) {
      setState(() {
        _rendimento = 'R\$' + (_deposito * 1.05).toString();
      });
    } else {
      setState(() {
        _rendimento = 'Valor Inválido.';
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
          title: Text('Poupança'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              TextField(
                controller: _controller1,
                decoration: InputDecoration(
                  labelText: 'Valor do depósito:'
                ),
              ),
              SizedBox(
                height: 32,
              ),
              FilledButton(onPressed: _poupanca, child: Text('Rendimento')),
              TextField(
                decoration: InputDecoration(
                  labelText: 'Resultado do rendimento em 1 mês'
                ),
                readOnly: true,
                controller: TextEditingController(text: _rendimento),
              ),
            ],
          ),
          ),
      ),
    );
  }
}
