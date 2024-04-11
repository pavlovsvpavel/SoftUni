function search() {
   const searchPattern = document.getElementById('searchText').value.trim().toLowerCase();
   const listOfTowns = document.querySelectorAll('#towns li');

//    listOfTowns.forEach(town => {
//       town.style.fontWeight = '';
//       town.style.textDecoration = 'none';
//   });

   let matches = 0;

   if (searchPattern !== "") {
      for (const town of listOfTowns) {
         if (town.textContent.toLowerCase().includes(searchPattern)) {
            matches += 1;
            town.style.fontWeight = 'bold';
            town.style.textDecoration = 'underline';
         }
      }
   }
   
   let resultDiv = document.getElementById('result')
   resultDiv.textContent = `${matches} matches found`
}
