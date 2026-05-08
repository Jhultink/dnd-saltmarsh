import clsx from 'clsx';
import Heading from '@theme/Heading';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

const FeatureList = [
  {
    emoji: '⚔️',
    title: 'Player Characters',
    description: 'Short Stacks, Snacks, and Lok — the adventurers navigating the dangers of Saltmarsh and beyond.',
    link: '/docs/characters/pcs/short-stacks',
    linkLabel: 'Meet the Party',
  },
  {
    emoji: '📜',
    title: '15 Sessions',
    description: 'From the haunted house on the cliff to the conspiracies threatening Saltmarsh itself — all recapped.',
    link: '/docs/sessions-recaps/session-15-confessions-at-the-docks',
    linkLabel: 'Latest Session',
  },
  {
    emoji: '🐉',
    title: 'NPCs & Allies',
    description: 'Allies, enemies, and everything in between — including a cursed dragon who went by Winston.',
    link: '/docs/characters/allies/winston',
    linkLabel: 'Browse Characters',
  },
];

function Feature({emoji, title, description, link, linkLabel}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center" style={{fontSize: '4rem', lineHeight: 1.2, padding: '1rem 0'}}>
        {emoji}
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
        <Link className="button button--primary button--sm" to={link}>
          {linkLabel}
        </Link>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
