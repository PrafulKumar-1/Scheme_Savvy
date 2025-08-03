
// FILE: frontend/src/features/1_Profiling/ProfilingForm.js
// The questionnaire form is now its own feature component.
import React, { useState } from 'react';
import {
  Box,
  VStack,
  FormControl,
  FormLabel,
  Input,
  Select,
  Button,
  SimpleGrid,
  useToast,
  FormErrorMessage
} from '@chakra-ui/react';
import { findSchemes } from '../../api/apiClient';

const ProfilingForm = ({ setIsLoading, setError, setSchemes }) => {
  const [profile, setProfile] = useState({
    age: '',
    state: 'Gujarat',
    occupation: '',
    income: '',
    gender: '',
  });
  const [formErrors, setFormErrors] = useState({});
  const toast = useToast();

  const validateForm = () => {
    const errors = {};
    if (!profile.age) errors.age = 'Age is required.';
    if (profile.age && (profile.age < 1 || profile.age > 120)) errors.age = 'Please enter a valid age.';
    if (!profile.occupation) errors.occupation = 'Occupation is required.';
    if (!profile.income) errors.income = 'Income is required.';
    if (profile.income && profile.income < 0) errors.income = 'Income cannot be negative.';
    if (!profile.gender) errors.gender = 'Gender is required.';
    setFormErrors(errors);
    return Object.keys(errors).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    setIsLoading(true);
    setError('');
    setSchemes([]);

    try {
      const response = await findSchemes(profile);
      setSchemes(response.data);
      if (response.data.length === 0) {
        toast({
          title: 'No schemes found.',
          description: "We couldn't find schemes matching your profile. Try adjusting your answers.",
          status: 'info',
          duration: 5000,
          isClosable: true,
        });
      }
    } catch (err) {
      const errorMessage = err.response?.data?.detail || 'An unexpected server error occurred.';
      setError(errorMessage);
      toast({
        title: 'An error occurred.',
        description: errorMessage,
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Box w="100%" p={8} borderWidth={1} borderRadius="lg" shadow="lg" bg="white">
      <form onSubmit={handleSubmit}>
        <VStack spacing={4}>
          <SimpleGrid columns={{ base: 1, md: 2 }} spacing={6} w="100%">
            <FormControl isRequired isInvalid={formErrors.age}>
              <FormLabel>Age</FormLabel>
              <Input name="age" type="number" placeholder="e.g., 25" onChange={handleChange} value={profile.age} />
              <FormErrorMessage>{formErrors.age}</FormErrorMessage>
            </FormControl>
            <FormControl isRequired>
              <FormLabel>State of Residence</FormLabel>
              <Select name="state" onChange={handleChange} value={profile.state}>
                <option value="Gujarat">Gujarat</option>
                <option value="Maharashtra">Maharashtra</option>
                <option value="Delhi">Delhi</option>
              </Select>
            </FormControl>
            <FormControl isRequired isInvalid={formErrors.occupation}>
              <FormLabel>Occupation</FormLabel>
              <Select name="occupation" placeholder="Select occupation" onChange={handleChange} value={profile.occupation}>
                <option value="Student">Student</option>
                <option value="Farmer">Farmer</option>
                <option value="Unemployed">Unemployed</option>
                <option value="Salaried">Salaried</option>
                <option value="Business Owner">Business Owner</option>
              </Select>
               <FormErrorMessage>{formErrors.occupation}</FormErrorMessage>
            </FormControl>
            <FormControl isRequired isInvalid={formErrors.income}>
              <FormLabel>Annual Family Income (in Lakhs)</FormLabel>
              <Input name="income" type="number" step="0.1" placeholder="e.g., 4.5" onChange={handleChange} value={profile.income} />
               <FormErrorMessage>{formErrors.income}</FormErrorMessage>
            </FormControl>
            <FormControl isRequired isInvalid={formErrors.gender}>
              <FormLabel>Gender</FormLabel>
              <Select name="gender" placeholder="Select gender" onChange={handleChange} value={profile.gender}>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Other">Other</option>
              </Select>
               <FormErrorMessage>{formErrors.gender}</FormErrorMessage>
            </FormControl>
          </SimpleGrid>
          <Button type="submit" colorScheme="teal" size="lg" w="full" mt={4}>
            Find My Schemes
          </Button>
        </VStack>
      </form>
    </Box>
  );
};

export default ProfilingForm;