class MusicService:
    def __init__(self):
        # Parâmetros Iniciais (Default)
        self.default_octave = 4
        self.max_octave = 9
        self.max_volume = 127 # Padrão máximo do MIDI
        
        self.current_volume = 64
        self.current_octave = self.default_octave
        self.current_instrument = 0
        
    def gerar_sequencia(self, texto: str) -> list[dict]:
        sequencia = []
        caractere_anterior_era_nota = False
        ultima_nota = None
        
        # O for no Python já faz o papel do "split" iterando letra por letra
        for char in texto:
            is_nota_atual = False
            acao = None
            
            # O match/case é o nosso "switch"
            match char:
                # Notas Diretas
                case 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G':
                    ultima_nota = char
                    is_nota_atual = True
                    acao = self._montar_nota(char)
                    
                case 'H':
                    ultima_nota = 'Bb' # Si Bemol
                    is_nota_atual = True
                    acao = self._montar_nota('Bb')
                    
                # Pausas Explícitas
                case 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h':
                    acao = {"evento": "PAUSA"}
                    
                # Alterações de Volume
                case ' ':
                    self.current_volume = min(self.current_volume * 2, self.max_volume)
                    
                # Alterações de Instrumento
                case '!':
                    self.current_instrument = 24
                case 'O' | 'o' | 'I' | 'i' | 'U' | 'u':
                    self.current_instrument = 110
                case '\n':
                    self.current_instrument = 123
                case ';':
                    self.current_instrument = 15
                case ',':
                    self.current_instrument = 114
                    
                # Regras com Dígitos usando "Guards" (if dentro do case)
                case c if c.isdigit() and int(c) % 2 == 0: # Dígito Par
                    self.current_instrument += int(c)
                case c if c.isdigit() and int(c) % 2 != 0: # Dígito Ímpar
                    self.current_instrument = 15
                    
                # Alterações de Oitava
                case '?' | '.':
                    self.current_octave += 1
                    if self.current_octave > self.max_octave:
                        self.current_octave = self.default_octave
                        
                # Regra ELSE (Consoantes restantes e qualquer outro caractere)
                case _:
                    if caractere_anterior_era_nota and ultima_nota:
                        acao = self._montar_nota(ultima_nota)
                        # A regra diz "se o ANTERIOR era nota A-H", o caractere atual 
                        # é uma consoante, então ele mesmo não conta como nota para o próximo.
                    else:
                        acao = {"evento": "PAUSA"}

            # Se gerou uma ação (Nota ou Pausa), adicionamos na lista final
            if acao:
                sequencia.append(acao)
                
            # Atualiza a flag para a próxima iteração do loop
            caractere_anterior_era_nota = is_nota_atual
            
        return sequencia

    def _montar_nota(self, nota: str) -> dict:
        """Função auxiliar para montar o objeto da nota com o estado atual"""
        return {
            "evento": "TOCAR_NOTA",
            "nota": nota,
            "oitava": self.current_octave,
            "volume": self.current_volume,
            "instrumento": self.current_instrument
        }