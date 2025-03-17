import 'package:flutter/material.dart';

class Bicicleta extends StatefulWidget {
  const Bicicleta({super.key});

  @override
  _BicicletaState createState() => _BicicletaState();
}

class _BicicletaState extends State<Bicicleta> {
  final TextEditingController _numEmpregadosController = TextEditingController();
  final TextEditingController _salarioMinimoController = TextEditingController();
  final TextEditingController _precoCustoController = TextEditingController();
  final TextEditingController _numBicicletasVendidasController = TextEditingController();
  String _resultado = '';

  void _calcular() {
    final int? numEmpregados = int.tryParse(_numEmpregadosController.text);
    final double? salarioMinimo = double.tryParse(_salarioMinimoController.text);
    final double? precoCusto = double.tryParse(_precoCustoController.text);
    final int? numBicicletasVendidas = int.tryParse(_numBicicletasVendidasController.text);

    if (numEmpregados != null &&
        salarioMinimo != null &&
        precoCusto != null &&
        numBicicletasVendidas != null) {

      final double salarioBase = 2 * salarioMinimo;
      final double comissaoPorBicicleta = precoCusto * 0.15;
      final double comissaoTotal = comissaoPorBicicleta * numBicicletasVendidas;
      final double comissaoPorEmpregado = comissaoTotal / numEmpregados;
      final double salarioFinalPorEmpregado = salarioBase + comissaoPorEmpregado;

      final double precoVenda = precoCusto * 1.5;
      final double receita = precoVenda * numBicicletasVendidas;
      final double lucroLiquido = receita - (precoCusto * numBicicletasVendidas) - (salarioFinalPorEmpregado * numEmpregados);

      setState(() {
        _resultado = '''
Salário Final por Empregado: R\$ ${salarioFinalPorEmpregado.toString()}
Lucro Líquido da Loja: R\$ ${lucroLiquido.toString()}
        ''';
      });
    } else {
      setState(() {
        _resultado = 'Por favor, insira valores válidos para todos os campos.';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Cálculo de Bicicletas'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: _numEmpregadosController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(
                labelText: 'Número de Empregados:',
              ),
            ),
            TextField(
              controller: _salarioMinimoController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(
                labelText: 'Salário Mínimo:',
              ),
            ),
            TextField(
              controller: _precoCustoController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(
                labelText: 'Preço de Custo da Bicicleta:',
              ),
            ),
            TextField(
              controller: _numBicicletasVendidasController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(
                labelText: 'Número de Bicicletas Vendidas:',
              ),
            ),
            const SizedBox(height: 20),
            FilledButton(
              onPressed: _calcular,
              child: const Text('Calcular'),
            ),
            const SizedBox(height: 20),
            Text(
              _resultado,
              style: const TextStyle(fontSize: 16),
              textAlign: TextAlign.left,
            ),
          ],
        ),
      ),
    );
  }
}
