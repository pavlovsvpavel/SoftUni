function solve() {
  function createElementAndAppendToOutput() {
    createPElement = document.createElement('p');
    createPElement.textContent = threeSentencesArr.join('.') + '.';
    outputDiv.appendChild(createPElement);
  }

  let text = document.getElementById('input');
  let sentences = text.value.split('.').filter((el) => el.length !== 0);

  let outputDiv = document.getElementById('output');
  let threeSentencesArr = [];
  for (let sentence of sentences) {
    if (threeSentencesArr.length === 3) {
      createElementAndAppendToOutput();
      threeSentencesArr = [];
    }
    threeSentencesArr.push(sentence);
  }

  createElementAndAppendToOutput();
  text.value = '';
}