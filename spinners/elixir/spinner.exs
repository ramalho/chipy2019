#! /usr/bin/env elixir

defmodule Spinner do
  @spinner_chars String.graphemes("⠇⠋⠙⠸⠴⠦")
  def spin(msg, char_idx \\ 0) do
    char = Enum.at(@spinner_chars, char_idx)
    status = "\r#{char} #{msg}"

    receive do
      {super_pid, :computed} ->
        blanks = String.duplicate(" ", String.length(status))
        IO.write("\r#{blanks}\r")
        send(super_pid, :done)
    after
      100 ->
        IO.write(status)
        spin(msg, rem(char_idx + 1, length(@spinner_chars)))
    end
  end

  def slow_function() do
    Process.sleep(3000)
    42
  end

  def supervisor() do
    pid = spawn(fn -> spin("thinking!") end)
    result = slow_function()
    send(pid, {self(), :computed})

    receive do
      :done -> result
    end
  end

  def main() do
    result = supervisor()
    IO.puts("Answer: #{result}")
  end
end

Spinner.main()
