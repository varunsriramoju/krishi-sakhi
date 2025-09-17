import React, {useState} from 'react'
import { useTranslation } from 'react-i18next'
import axios from 'axios'
import LanguageSwitcher from './components/LanguageSwitcher'

export default function App(){
  const { t, i18n } = useTranslation()
  const [text, setText] = useState('')
  const [chat, setChat] = useState([])
  const send = async ()=>{
    if(!text) return
    const payload = { user:{id:1,name:'Demo'}, farm:{id:1,name:'DemoFarm'}, text, language: i18n.language }
    const r = await axios.post('http://localhost:8000/api/advisory/generate', payload)
    setChat(c=>[...c, {in:text, out:r.data.advisory}])
    setText('')
  }
  return (<div style={{maxWidth:700, margin:'40px auto', fontFamily: 'sans-serif'}}>
    <h2>{t('welcome')}</h2>
    <LanguageSwitcher />
    <div style={{marginTop:20}}>
      <textarea value={text} onChange={e=>setText(e.target.value)} rows={4} style={{width:'100%'}} placeholder={t('enter_issue')} />
      <button onClick={send} style={{marginTop:8}}>{t('ask')}</button>
    </div>
    <div style={{marginTop:20}}>
      {chat.map((c,i)=>(<div key={i} style={{padding:10,border:'1px solid #eee', marginBottom:8}}>
        <b>Q:</b> {c.in}<br/><b>A:</b> {c.out}
      </div>))}
    </div>
  </div>)
}
