@esqueceu_a_senha
Feature: Esqueceu a senha

  Scenario Outline: Usuarios com Cadastro
    Given que acesso o site Blazedemo
    When clico em Home
    And clico no link Forgot Your Password?
    Then vejo a página de reiniciar a senha
    When preencho meu "<email>" e clico no botao Send Password Reset Link
    Then vejo a mensagem de confirmacao
    Examples:
      | email                     |
      | trovadorandante@gmail.com |
      | teste@teste.com           |
