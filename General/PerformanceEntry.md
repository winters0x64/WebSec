# PerformanceEntry

So basically it measures resource loading time mostly used for performance analysis this could be used as a way to view past requests made if you have in hand an XSS.

```js
function captureNetworkRequest(e) {
    var capture_network_request = [];
    var capture_resource = performance.getEntriesByType("resource");
    for (var i = 0; i < capture_resource.length; i++) {
                capture_network_request.push(capture_resource[i].name)

        }

    return capture_network_request;
}
```