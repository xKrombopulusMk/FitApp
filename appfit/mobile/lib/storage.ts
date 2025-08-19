import AsyncStorage from '@react-native-async-storage/async-storage'

export async function setToken(t: string) {
  await AsyncStorage.setItem('token', t)
}

export async function getToken() {
  return AsyncStorage.getItem('token')
}
