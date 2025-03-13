import 'package:flutter/material.dart';

const String accountName = "Xx.Panda.xX";
const String accountEmail = "pandaofc@gmail.com";

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
      appBar: AppBar(
        title: const Text('🐼 Panda',
            style: TextStyle(
                color: Color(0xd5ffffff), fontWeight: FontWeight.bold)),
        backgroundColor: Colors.grey,
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            const UserAccountsDrawerHeader(
              accountName: Text(accountName),
              accountEmail: Text(accountEmail),
              currentAccountPicture: CircleAvatar(
                backgroundColor: Colors.white,
                child: ClipOval(
                  child: Image(
                    image: NetworkImage(
                        'https://th.bing.com/th/id/R.973216a8c6a6a1c27707b7ff97444a13?rik=8cNMPsiliD%2b1yg&riu=http%3a%2f%2fstatic.artfcity.com%2fwp-content%2fuploads%2f2013%2f10%2fCute-Panda-Bears-animals-34916401-1455-1114.jpg&ehk=buQOdQh3omPv6IraYH%2bnlLgHNBE58nY2y5RN13FrjhI%3d&risl=&pid=ImgRaw&r=0'),
                    fit: BoxFit.cover,
                    width: 90.0,
                    height: 90.0,
                  ),
                ),
              ),
              decoration: BoxDecoration(
                color: Colors.grey,
              ),
            ),
            ListTile(
              leading: const Icon(Icons.account_box),
              title: const Text("Profile"),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const ProfileInfo()),
                );
              },
            ),
          ],
        ),
      ),
      backgroundColor: const Color(0xd514122b),
      body: const Center(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Expanded(
              child: Text('PANDA',
                  style: TextStyle(color: Colors.white, fontSize: 24)),
            ),
            Expanded(
              child: Image(
                image: NetworkImage(
                    'https://th.bing.com/th/id/R.973216a8c6a6a1c27707b7ff97444a13?rik=8cNMPsiliD%2b1yg&riu=http%3a%2f%2fstatic.artfcity.com%2fwp-content%2fuploads%2f2013%2f10%2fCute-Panda-Bears-animals-34916401-1455-1114.jpg&ehk=buQOdQh3omPv6IraYH%2bnlLgHNBE58nY2y5RN13FrjhI%3d&risl=&pid=ImgRaw&r=0'),
              ),
            )
          ],
        ),
      ),
    );
  }
}

class ProfileInfo extends StatelessWidget {
  const ProfileInfo({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: GestureDetector(
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const HomeScreen()),
            );
          },
          child: const Text(
            '🐼 Panda',
            style: TextStyle(
                color: Color(0xd5ffffff), fontWeight: FontWeight.bold),
          ),
        ),
        backgroundColor: Colors.grey,
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            const UserAccountsDrawerHeader(
              accountName: Text(accountName),
              accountEmail: Text(accountEmail),
              currentAccountPicture: CircleAvatar(
                backgroundColor: Colors.white,
                child: ClipOval(
                  child: Image(
                    image: NetworkImage(
                        'https://th.bing.com/th/id/R.973216a8c6a6a1c27707b7ff97444a13?rik=8cNMPsiliD%2b1yg&riu=http%3a%2f%2fstatic.artfcity.com%2fwp-content%2fuploads%2f2013%2f10%2fCute-Panda-Bears-animals-34916401-1455-1114.jpg&ehk=buQOdQh3omPv6IraYH%2bnlLgHNBE58nY2y5RN13FrjhI%3d&risl=&pid=ImgRaw&r=0'),
                    fit: BoxFit.cover,
                    width: 90.0,
                    height: 90.0,
                  ),
                ),
              ),
              decoration: BoxDecoration(
                color: Colors.grey,
              ),
            ),
            ListTile(
              leading: const Icon(Icons.account_box),
              title: const Text("Profile"),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const ProfileInfo()),
                );
              },
            ),
          ],
        ),
      ),
      backgroundColor: const Color(0xd514122b),
      body: const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Expanded(
                  child: Text(accountName,
                      style: TextStyle(
                          color: Colors.blue,
                          fontSize: 32,
                          fontWeight: FontWeight.bold)),
                ),
                Expanded(
                  child: Text(
                    "Idade: 400 anos",
                    style: TextStyle(
                        fontStyle: FontStyle.italic,
                        color: Colors.red,
                        fontSize: 24),
                  ),
                ),
                Expanded(
                  child: Text(
                    "Cidade: Campo Granders",
                    style: TextStyle(color: Colors.purple, fontSize: 24),
                  ),
                )
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Expanded(
                  child: Text('Nome',
                      style: TextStyle(
                          color: Colors.blue,
                          fontSize: 28,
                          fontWeight: FontWeight.bold)),
                ),
                Expanded(
                  child: Text(
                    "Idade",
                    style: TextStyle(
                        fontStyle: FontStyle.italic,
                        color: Colors.green,
                        fontSize: 22),
                  ),
                )
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Expanded(
                  child: Text('Nome',
                      style: TextStyle(
                          color: Colors.orange,
                          fontSize: 26,
                          fontWeight: FontWeight.bold)),
                ),
                Expanded(
                  child: Text(
                    "Idade",
                    style: TextStyle(
                        fontStyle: FontStyle.italic,
                        color: Colors.red,
                        fontSize: 20),
                  ),
                )
              ],
            ),
          ],
        ),
      ),
    );
  }
}
