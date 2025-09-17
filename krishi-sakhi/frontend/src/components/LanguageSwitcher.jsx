import React from 'react'
import { useTranslation } from 'react-i18next'

export default function LanguageSwitcher(){
  const { i18n } = useTranslation()
  const setLang = (l)=> i18n.changeLanguage(l)
  return (<div>
    <button onClick={()=>setLang('ml')}>മലയാളം</button>
    <button onClick={()=>setLang('en')}>English</button>
  </div>)
}
