package kyu5;

import java.util.HashMap;
import java.util.Map;

public class SimpleAssembler {
	private static Map<String, Integer> reg = new HashMap<String, Integer>();
	private static int pc = 0;

	public static Map<String, Integer> interpret(String[] program) {
		reg = new HashMap<String, Integer>();
		pc = 0;

		while (pc < program.length) {
			String[] instr = program[pc].split(" ");
			switch (instr[0]) {
			case "mov":
				mov(instr[1], instr[2]);
				break;
			case "inc":
				inc(instr[1]);
				break;
			case "dec":
				dec(instr[1]);
				break;
			case "jnz":
				jnz(instr[1], instr[2]);
				break;
			}
		}
		return reg;
	}

	private static void mov(String r, String v) {
		Integer val = v.matches("[a-z]*") ? reg.get(v) : Integer.valueOf(v);
		reg.put(r, val);
		++pc;
	}

	private static void inc(String r) {
		reg.put(r, reg.get(r) + 1);
		++pc;
	}

	private static void dec(String r) {
		reg.put(r, reg.get(r) - 1);
		++pc;
	}

	private static void jnz(String v, String j) {
		pc += ((v.matches("\\d") && Integer.parseInt(v) != 0) || (reg.containsKey(v) && reg.get(v) != 0))
				? Integer.parseInt(j)
				: 1;
	}
}