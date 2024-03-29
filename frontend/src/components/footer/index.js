import { Container, LinkComponent } from '../index'
import styles from './style.module.css'

const Footer = () => {
  return <footer className={styles.footer}>
      <Container className={styles.footer__container}>
        <LinkComponent href='/recipes/' title='Продуктовый помощник' className={styles.footer__brand} />
      </Container>
  </footer>
}

export default Footer
