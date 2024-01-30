# Window.PostMessage

window.postMessage(data,origin) can send data to the speicifed origin supports Cross Origin requests, if envoked with ``let tw = window.opener('http://91.107.157.58:7000/')`` and then ``tw.postMessage('<h1>Hello</h1>','http://91.107.157.58:7000/')``, Since the origin that you are sending should be the same as the sending window's origin. Hence the opener policy works here.
