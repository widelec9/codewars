package kyu5;

import java.util.LinkedHashMap;
import java.util.Map;

public class FixmeHello {
	private Map<String, String> dataMap = new LinkedHashMap<>();

	public FixmeHello() {
		dataMap.put("hello", "Hello.");
	}

	public FixmeHello setAge(int age) {
		dataMap.put("age", String.format("I am %d.", age));
		return this;
	}

	public FixmeHello setSex(char sex) {
		dataMap.put("sex", String.format("I am %s.", sex == 'F' ? "female" : "male"));
		return this;
	}

	public FixmeHello setName(String name) {
		dataMap.put("name", String.format("My name is %s.", name));
		return this;
	}

	public String hello() {
		return String.join(" ", dataMap.values());
	}
}