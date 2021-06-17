let runaTexto = document.querySelector("#texto");
let imagem = document.querySelector("#imagemRuna");

const botao = document.querySelector("#botao");
const imagensRunas = document.querySelectorAll('.imagensCadrArt')

const imagemCardArt = [];

for (let i = 0; i < imagensRunas.length; i++) {
   imagemCardArt.push(imagensRunas[i].getAttribute('src'))
  
}

let atributosRunas;
let nomesrunas;

function escolhido() {
  const escolhaRuna = document.getElementsByClassName("escolhaRuna");

  for (let i = 0; i < escolhaRuna.length; i++)
    if (escolhaRuna[i].checked) {
      escolhaRuna[i].parentElement.style.transition = "all 1s";
      escolhaRuna[i].parentElement.style.borderColor = "red";
      escolhaRuna[i].parentElement.style.boxShadow = "0 0 10px darkred";
      nomesRunas = escolhaRuna[i].value;
      atributosRunas = i;
    } else {
      escolhaRuna[i].parentElement.style.borderColor = "";
      escolhaRuna[i].parentElement.style.boxShadow = "";
    }
}

botao.addEventListener("click", () => {
  imagem.setAttribute("src", imagemCardArt[atributosRunas]);
  imagem.style.borderRadius = "7rem";
  imagem.style.width = "12rem";
  runaTexto.innerHTML = nomesRunas;
});
