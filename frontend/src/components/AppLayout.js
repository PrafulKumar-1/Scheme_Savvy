// FILE: frontend/src/components/AppLayout.js
import React from 'react';
import { Box, Flex, Heading, Link, Button, Container } from '@chakra-ui/react';
import { Link as RouterLink, useLocation } from 'react-router-dom';

const NavLink = ({ to, children }) => {
  const location = useLocation();
  const isActive = location.pathname === to;
  return (
    <Link as={RouterLink} to={to} fontWeight={isActive ? 'bold' : 'normal'}>
      <Button variant="ghost" _hover={{ bg: 'teal.600' }} isActive={isActive}>
        {children}
      </Button>
    </Link>
  );
};

const AppLayout = ({ children }) => {
  return (
    <Box>
      <Flex
        as="nav"
        align="center"
        justify="space-between"
        wrap="wrap"
        padding="1.5rem"
        bg="teal.500"
        color="white"
        boxShadow="sm"
      >
        <Flex align="center" mr={5}>
          <Link as={RouterLink} to="/" _hover={{ textDecoration: 'none' }}>
            <Heading as="h1" size="lg" letterSpacing={'-.1rem'}>
              SchemeSavvy
            </Heading>
          </Link>
        </Flex>
        <Box>
          <NavLink to="/">Scheme Finder</NavLink>
          <NavLink to="/vision">Our Vision</NavLink>
        </Box>
      </Flex>
      <Container maxW="container.xl" pt={8} pb={8}>
        {children}
      </Container>
    </Box>
  );
};

export default AppLayout;