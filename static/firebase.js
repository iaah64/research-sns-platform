// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyBbuIeqozeO7IwB0VFcVjT6xBo9csn7WS0",
  authDomain: "research-sns-platform.firebaseapp.com",
  databaseURL: "https://research-sns-platform.firebaseio.com",
  projectId: "research-sns-platform",
  storageBucket: "research-sns-platform.appspot.com",
  messagingSenderId: "692500729773",
  appId: "1:692500729773:web:0b31c32e5c61715e8e5b24",
  measurementId: "G-5GL9VGKGZS"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

var db = firebase.database();
