import React, { Component } from 'react';
import { AppRegistry, Text, View } from 'react-native';
import { StackNavigator } from 'react-navigation';

import Component1 from './app/components/Component1/Component1'
import Component2 from './app/components/Component2/Component2'
import Component3 from './app/components/Component3/Component3'
import Component4 from './app/components/Component4/Component4'
import Component5 from './app/components/Component5/Component5'
import Component6 from './app/components/Component6/Component6'

const RootNavigator = StackNavigator ({
  Home : {
    screen : Component5,
    navigationOptions : {
      headerTitle : 'Home',
    },
  },
  Details : {
    screen : Component6,
    navigationOptions : {
      headerTitle : 'Details',
    },
  },
});

export default class App extends Component {

  static navigationOptions = {
    title : 'Home',
  }

  render () {
    return (
      <RootNavigator />
    );
  }
}

AppRegistry.registerComponent ('App', () => App);