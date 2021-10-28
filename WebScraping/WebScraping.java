import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * @author Vincent
 */
public class WebScraping {
    public static int BYTE_SIZE = 63;
    public static int STANDARD_OFFSET = 0;
    public static String ERROR_OUTPUT = "";

    /**
     *
     * @param args url链接
     */
    public static void main(String[] args) {
        String url1 = "http://pythonscraping.com/files/MontyPythonAlbums.csv";
        String url2 = "http://pythonscraping.com/files/MontyPythonAlbums.csv";
        String url3 = "http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt";

        System.out.println(getWebString(url1));
        System.out.println("-------------");
        System.out.println(getWebString2(url2));
        System.out.println("-------------");
        System.out.println(getWebString2(url3));
    }

    /**
     * 使用字节数组转成字符串
     *
     * @param webUrl url链接
     * @return 字符串处理结果
     */
    public static String getWebString(String webUrl) {
        try {
            URL url = new URL(webUrl);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            urlConnection.connect();
            int len = urlConnection.getContentLength();
            InputStream inputStream = urlConnection.getInputStream();

            int i = 0;
            StringBuilder sb = new StringBuilder();
            while (i < len) {
                byte[] bytes;
                if (len - i <= BYTE_SIZE) {
                    bytes = new byte[len - i];
                    inputStream.read(bytes, STANDARD_OFFSET, len - i);
                } else {
                    bytes = new byte[BYTE_SIZE];
                    inputStream.read(bytes, STANDARD_OFFSET, BYTE_SIZE);
                }
                sb.append(new String(bytes));
                i += BYTE_SIZE;
            }
            inputStream.close();

            return sb.toString();
        } catch (Exception e) {
            return ERROR_OUTPUT;
        }
    }

    /**
     * 使用BuffedReader读取
     *
     * @param webUrl url链接
     * @return 字符串处理结果
     */
    public static String getWebString2(String webUrl) {
        try {
            URL url = new URL(webUrl);
            InputStream inputStream = url.openStream();
            InputStreamReader inputStreamReader = new InputStreamReader(inputStream, "UTF-8");
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
            String line;
            StringBuilder sb = new StringBuilder();
            while ((line = bufferedReader.readLine()) != null) {
                sb.append(line);
                sb.append("\r\n");
            }

            return sb.toString();
        } catch (Exception e) {
            return ERROR_OUTPUT;
        }
    }
}
