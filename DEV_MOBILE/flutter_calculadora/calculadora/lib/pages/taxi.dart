import 'package:flutter/material.dart';

class Taxi extends StatefulWidget {
  const Taxi({super.key});

  @override
  _TaxiState createState() => _TaxiState();
}

class _TaxiState extends State<Taxi> {
  final TextEditingController _controller1 = TextEditingController();
  final TextEditingController _controller2 = TextEditingController();
  final TextEditingController _controller3 = TextEditingController();
  final TextEditingController _controller4 = TextEditingController();
  String _mediaConsumo = '';
  String _lucroLiquido = '';

  void _calcular() {
    final double hodometroInicial = double.tryParse(_controller1.text) ?? 0.0;
    final double hodometroFinal = double.tryParse(_controller2.text) ?? 0.0;
    final double litrosGastos = double.tryParse(_controller3.text) ?? 0.0;
    final double valorRecebido = double.tryParse(_controller4.text) ?? 0.0;

    if (hodometroFinal >= hodometroInicial && litrosGastos > 0) {
      final double distanciaPercorrida = hodometroFinal - hodometroInicial;
      final double mediaConsumo = distanciaPercorrida / litrosGastos;
      final double precoCombustivel = 2.50;
      final double custoCombustivel = litrosGastos * precoCombustivel;
      final double lucroLiquido = valorRecebido - custoCombustivel;

      setState(() {
        _mediaConsumo = mediaConsumo.toStringAsFixed(2);
        _lucroLiquido = lucroLiquido.toStringAsFixed(2);
      });
    } else {
      setState(() {
        _mediaConsumo = 'Valores inválidos.';
        _lucroLiquido = 'Valores inválidos.';
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
          title: Text('Rendimento'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              TextField(
                controller: _controller1,
                decoration: InputDecoration(
                  labelText: 'Hodômetro (Km) no início do dia:'
                ),
                keyboardType: TextInputType.number,
              ),
              TextField(
                controller: _controller2,
                decoration: InputDecoration(
                  labelText: 'Hodômetro (Km) no fim do dia:'
                ),
                keyboardType: TextInputType.number,
              ),
              TextField(
                controller: _controller3,
                decoration: InputDecoration(
                  labelText: 'Número de litros gastos:'
                ),
                keyboardType: TextInputType.number,
              ),
              TextField(
                controller: _controller4,
                decoration: InputDecoration(
                  labelText: 'Valor recebido dos passageiros:'
                ),
                keyboardType: TextInputType.number,
              ),
              SizedBox(height: 32),
              ElevatedButton(
                onPressed: _calcular,
                child: Text('Calcular'),
              ),
              SizedBox(height: 16),
              TextField(
                decoration: InputDecoration(
                  labelText: 'Média de consumo (Km/L)'
                ),
                readOnly: true,
                controller: TextEditingController(text: _mediaConsumo),
              ),
              TextField(
                decoration: InputDecoration(
                  labelText: 'Lucro líquido (R\$)'
                ),
                readOnly: true,
                controller: TextEditingController(text: _lucroLiquido),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
