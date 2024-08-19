from flask import Flask, render_template, request

class app04():
    def __init__(self):
        self.app = Flask(__name__)
        self.defineRotas()

    def defineRotas(self):
        @self.app.route('/')
    #     def index():
    #         return render_template('index.html')
        
    #     @self.app.route('/form01')
    #     def rotaForm01():
    #         return render_template('form01.html')

    #     @self.app.route('/form01_submit' , methods=['POST'])
    #     def rotaForm01_Submit():
    #         nome = request.form.get('nome')
    #         return render_template('form01.html', dados = nome)



#desafio02

        # @self.app.route('/formCalc')
        # def rotaFormCalc():
        #     return render_template('formCalc.html')
        
        # @self.app.route('formCalc_submit', methods= ['POST'])
        # def formCalc_submit():
        #     num1 = request.form.get('num1')
        #     num2 = request.form.get('num2')
        #     soma = int(num1) + int(num2)
        #     return f'esse é o resultado: {soma}'

#desafio04

        # @self.app.route('/media_submit')
        # def media_submit():
        #     return render_template('media.html')
        
        # @self.app.route('/media_submit', methods=['POST'])
        # def media_submit():
        #     nota1 = request.form.get('nota1')
        #     nota2 = request.form.get('nota2')
        #     nota3 = request.form.get('nota3')
        #     media = (int(nota1) + int(nota2) + int(nota3))
        #     resultado = media / 3
        #     return f'essa é a média: {resultado}'
        
#desafio05
        
        # @self.app.route('/rotacm_submit')
        # def rotacm_submit():
        #     return render_template('rotacm.html')
        
        # @self.app.route('/rotacm_submit', methods=['POST'])
        # def rotacm_submit():
        #     cm = request.form.get('cm')
        #     metro= request.form.het('metros')
        #     resultado = metro / 100
        #     return f'essa é a conversão: {cm} cm é igual a {metro}'
        
#desafio06

#desafio07

#desafio08

#desafio09

#desafia10

        # @self.app.route('/quadrado')
        # def quadrado():
        #     return render_template('quadrado.html')
        
        # @self.app.route('/quadrado_submit' , methods=['POST'])
        # def quadrado_submit():
        #     lado = request.form.get('lado1')
        #     area = float(lado) * float(lado)
        #     volume = float(lado) * float(lado) * float(lado)
        #     return f'a área é: {area} , e o volume é: {volume}'

#desafio11

        # @self.app.route('/caracteres')
        # def caracteres():
        #     return render_template('caracteres.html')
        
        # @self.app.route('/caracteres_submit' , methods= ['POST'])
        # def quadrado_submit():
        #     texto = request.form.get('palavra')
        #     contagem = len(texto.strip())
        #     return f'essa é a contagem de caracteres: {contagem}'

#desafio12
        
        # @self.app.route('/trabalho')
        # def trabalho():
        #     return render_template('trabalho.html')
        
        # @self.app.route('/trabalho_submit' , methods= ['POST'])
        # def trabalho_submit():
        #     por_hora = request.form.get('por_hora')
        #     horas = request.form.get('horas')
        #     salario = float(por_hora) * float(horas)
        #     return f'seu salario é: {salario}'

#desafio13

        # @self.app.route('/quilometros')
        # def quilometros():
        #     return render_template('quilometros.html')
            
        # @self.app.route('/quilometros_submit' , methods= ["POST"])
        # def quilometros_submit():
        #     distancia = request.form.get('distancia')
        #     litro = float(distancia) / 12
        #     preco = float(litro) * 6.50
        #     return render_template('quilometros.html' , preco = preco)


if __name__ == '__main__':
    MeuApp = app04()
    MeuApp.app.run(debug=True)
