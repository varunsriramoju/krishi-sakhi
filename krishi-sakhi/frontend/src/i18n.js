import i18n from 'i18next'
import { initReactI18next } from 'react-i18next'
import en from './locales/en/translation.json'
import ml from './locales/ml/translation.json'

const resources = { en: {translation:en}, ml: {translation:ml} }

i18n.use(initReactI18next).init({
  resources,
  lng: 'ml',
  fallbackLng: 'en',
  interpolation: { escapeValue:false }
})

export default i18n
