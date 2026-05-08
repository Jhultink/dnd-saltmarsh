import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">A D&amp;D 5e campaign set in the port town of Saltmarsh</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/sessions-recaps/session-01-arrival-in-saltmarsh">
            Start from Session 1
          </Link>
          <Link
            className="button button--outline button--secondary button--lg"
            to="/docs/sessions-recaps/session-15-confessions-at-the-docks"
            style={{marginLeft: '1rem'}}>
            Latest Session
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="Campaign notes for a D&D 5e Ghosts of Saltmarsh campaign — session recaps, player characters, and NPCs.">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
