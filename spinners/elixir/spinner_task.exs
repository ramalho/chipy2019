#! /usr/bin/env elixir

defmodule Spinner do
  @spinner_chars String.graphemes("⠇⠋⠙⠸⠴⠦")
  def spin(computation, msg, char_idx \\ 0) do
    char = Enum.at(@spinner_chars, char_idx)
    status = "\r#{char} #{msg}"

    case Task.yield(computation, 100) do
      {:ok, result} ->
        blanks = String.duplicate(" ", String.length(status))
        IO.write("\r#{blanks}\r")
        result
      nil ->
        IO.write(status)
        char_idx = rem(char_idx + 1, length(@spinner_chars))
        spin(computation, msg, char_idx)
    end
  end

  def slow_function() do
    Process.sleep(3000)
    42
  end

  def supervisor() do
    computation = Task.async(&slow_function/0)
    spin(computation, "thinking!")
  end

  def main() do
    result = supervisor()
    IO.puts("Answer: #{result}")
  end
end

Spinner.main()
