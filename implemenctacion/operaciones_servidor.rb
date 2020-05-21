$:.push('gen-rb')

require 'thrift'
require 'Operaciones'


class OperacionesHandler  

  def sumar(num1, num2)    
    puts "Sumando #{num1}" + "+" + "#{num2}"
    return num1 + num2
  end

  def multiplicar(num1, num2)
    puts "Multiplicando #{num1}" + "*" + "#{num2}"
    return num1 * num2
  end

  def restar(num1, num2)
    puts "Restando #{num1}" + "-" + "#{num2}"
    return num1 - num2
  end

  def dividir(num1, num2)
    puts "Dividiendo #{num1}" + "/" + "#{num2}"
    return num1 / num2
  end  
end

handler = OperacionesHandler.new()
processor = Operaciones::Processor.new(handler)
transport = Thrift::ServerSocket.new(9090)
transportFactory = Thrift::BufferedTransportFactory.new()
server = Thrift::SimpleServer.new(processor, transport, transportFactory)

puts "Starting the server..."
server.serve()
puts "done."