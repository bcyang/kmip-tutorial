# Whatever

Something totally unrelated

### Sample Codes to do HTTP Get on Java

```
public httpGet(String targetUrl) {

    // configure HTTP client
    RequestConfig config = RequestConfig.custom()
            .setConnectTimeout(500)
            .setConnectionRequestTimeout(500)
            .setSocketTimeout(500)
            .setContentCompressionEnabled(true).build();
    CloseableHttpClient httpclient = HttpClientBuilder.create().setDefaultRequestConfig(config).build();

    // create the HTTP request, set headers, etc.
    HttpGet request = new HttpGet(targetUrl);
    request.addHeader(HttpHeaders.CONTENT_TYPE, "application/json");

    // execute the HTTP request
    try (CloseableHttpResponse response = httpclient.execute(request)) {
        HttpEntity entity = response.getEntity();
        InputStream is = entity.getContent();  // response content

        StringWriter writer = new StringWriter();
        IOUtils.copy(is, writer, "UTF-8");
        String jsonString = writer.toString();
        try {
            data = gson.fromJson(jsonString, unmarshallerType);
        } catch (Exception e) {
            // failed to unmarshall the JSON
        }
    } catch (Exception e) {
        // 
    }
}
```