import React from 'react';
import { DefaultView } from '@plone/volto/components';
import { Container } from 'semantic-ui-react';
import { Helmet } from '@plone/volto/helpers';

const PresentacionView = (props) => {
    const { content } = props;
    return (
        <Container id="view-wrapper presentacion-view">
        <Helmet title={content.title} />
        <h1 className="documentFirstHeading">
          <span className="type_of_presentacion">{content.description}: </span>
          {content.title}
        </h1>
        {content.description && (
          <p className="documentDescription">{content.description}</p>
        )}
        <div dangerouslySetInnerHTML={{ __html: content.details.data }} />
      </Container>);
};


export default PresentacionView;