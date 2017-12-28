import React, { Component } from 'react';
import { AppRegistry, Text, View } from 'react-native';

export default class Component6 extends Component {

    constructor (props) {
        super (props);
        const { state } = this.props.navigation;
        this.state = {
            name  : state.params.user.name,
            email : state.params.user.email, 
        }
    }

  render () {
    return (
      <View>
          <Text>Details : </Text>
          <Text> { this.state.name } </Text>
          <Text> { this.state.email } </Text>
      </View>
    );
  }
}

AppRegistry.registerComponent ('Component6', () => Component6);