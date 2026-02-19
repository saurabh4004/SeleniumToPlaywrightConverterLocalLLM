import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

PROMPT_SOP = """
You are an expert Test Automation Engineer. Convert this Selenium Java code to Playwright TypeScript.
Output STRICTLY CODE ONLY. No comments, no markup.
"""

JAVA_CODE = """
import java.time.Duration;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;

public class BaseTest {
    protected WebDriver driver;
    protected WebDriverWait wait;
    
    @BeforeClass
    public void setup() {
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        driver.get("https://the-internet.herokuapp.com/login");
    }
    
    @AfterClass
    public void tearDown() {
        driver.quit();
    }
}
"""

def test_qwen():
    payload = {
        "model": "qwen2.5:0.5b",
        "prompt": f"{PROMPT_SOP}\n\n{JAVA_CODE}",
        "stream": False
    }
    try:
        print("Testing qwen2.5:0.5b conversion...")
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
        print("Response received!")
        print("-" * 20)
        print(response.json().get("response"))
        print("-" * 20)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_qwen()
