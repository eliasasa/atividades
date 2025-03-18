import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.blue,
          title: Text('GridView Example'),
        ),
        body: GridView.builder(
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2, // colunas
            crossAxisSpacing: 8, // gap
            mainAxisSpacing: 8, // rowgap
          ),
          itemCount: 100,
          itemBuilder: (context, index) {
            return GestureDetector(
              onTap: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text('Você clicou no item $index')),
                );
              },
              child: Card(
                elevation: 4,
                child: Center(
                  child: Text(
                    'Item $index',
                    style: TextStyle(fontSize: 16),
                  ),
                ),
              ),
            );
          },
          padding: EdgeInsets.all(8),
        ),
      ),
    );
  }
}
