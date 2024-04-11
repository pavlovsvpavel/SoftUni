function solve() {
  const text = document.getElementById('text').value;
  const convention = document.getElementById('naming-convention').value;
  const resultDivElement = document.getElementById('result');

  let result = '';
  const textArray = text.toLowerCase().split(' ');

  if (!['Camel Case', 'Pascal Case'].includes(convention)) {
    result = 'Error!';
  } else {
    for (let word of textArray) {
      word = word[0].toUpperCase() + word.slice(1);
      result += word;
    }

    if (convention === 'Camel Case') {
      result = result[0].toLowerCase() + result.slice(1);
    }
  }

  resultDivElement.textContent = result;
}