describe('200 Status Code Check', () => {
  it('Checks status code is equal to 200', () => {
    cy.request('POST', '/').its('status').should('eq',200)
  })

  it('Checks response body returns a value', () => {
    cy.request('POST', '/').its('body').should('not.eq', null)
  })

})