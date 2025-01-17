import React from 'react';
import { AppRegistry, View, Text, StyleSheet } from 'react-native'

export default class Counter extends React.Component {

    state = {
        count : 0
    }

    componentDidMount () {
        setInterval (() => {
            this.setState ({
                count : this.state.count + 1
            })
        }, 1000)
    }

    render () {
        const { count } = this.state
        const { color, size } = this.props

        return (
            <Text style = {{ color, fontSize : size}}>
                { count }
            </Text>
        )
    }

}