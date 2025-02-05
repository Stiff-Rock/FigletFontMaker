import figlet from 'figlet';
try {
  console.log(JSON.stringify(figlet.fontsSync()));
} catch (err) {
  console.error('Error retrieving fonts:', err);
}
