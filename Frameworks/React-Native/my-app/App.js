import React from 'react';
import { AppRegistry, StyleSheet, Text, View } from 'react-native';
import Counter from "./Components/Counter" 

export default class App extends React.Component {
  render() {
    return (
      <View style = {styles.container}>
        <Counter color = {'lightblue'} size = {16} />
        <Counter color = {'skyblue'}   size = {32} />
        <Counter color = {'steelblue'} size = {80} />
        <Counter color = {'darkblue'}  size = {140} />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

AppRegistry.registerComponent('App', () => App)